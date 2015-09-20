import os
import random

from gensim.models import Doc2Vec

from helpers.data_path import model_data_path
from helpers.gensim_version_abstraction import save_doc2vec_model
from helpers.learning_rate_helper import alpha_for_epoch
from helpers.log_config import log_to_info
from helpers.random_helper import random_int
from hpv.hpv import convert_to_labeled_review
import time


class Doc2VecFactory:
    def __init__(self, mp, reviews, dm):
        self.mp = mp
        self.reviews = reviews
        self.workers = 8  # Number of threads to run in parallel
        self.min_count = mp.min_count  # Minimum word count
        self.dm = dm
        self.epochs = mp.epochs
        self.model = self.load_model(self.epochs)

    def model_path(self, epoch=None):
        return model_data_path('{0}-dm{1}.model'.format(self.mp.word2vec_model_path(epoch), self.dm))

    def load_model(self, epoch=None):
        path = self.model_path(epoch)
        return Doc2Vec.load(path) if os.path.isfile(path) else None

    def store_model(self, epoch):
        model_path = self.model_path(epoch)
        dir_path = os.path.dirname(model_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        save_doc2vec_model(self.model, model_path)

    def get_word2vec_model(self):
        if not self.model:
            self.train_model()

        self.model.init_sims(replace=True)
        return self.model

    def train_model(self):
        log_to_info('Loading training sentences')

        review_d2v_id_list = zip(self.reviews['words'], self.reviews['d2v_id'], self.reviews['best_topics'],
                                 self.reviews['second_best_topics'])

        labeled_reviews = []
        if self.dm == 0:
            log_to_info('applying dbow with hpv={}'.format(self.mp.hierarchical_paragraph_vectors_dbow))
        elif self.dm == 1:
            log_to_info('applying dm with hpv={}'.format(self.mp.hierarchical_paragraph_vectors_dm))
            
        for space_separated_words, d2v_id, best_topic, second_best_topic in review_d2v_id_list:
            if self.dm == 0:
                labeled_reviews.extend(
                    convert_to_labeled_review(self.mp.hierarchical_paragraph_vectors_dbow, space_separated_words, d2v_id, best_topic,
                                              second_best_topic))
            elif self.dm == 1:
                labeled_reviews.extend(
                    convert_to_labeled_review(self.mp.hierarchical_paragraph_vectors_dm, space_separated_words, d2v_id, best_topic,
                                              second_best_topic))

        log_to_info('Loading Doc2Vec model...')
        start_epoch = self.epochs + 1
        model = None
        for epoch in range(self.epochs, 0, -1):
            model = self.load_model(epoch)
            if model:
                log_to_info('Found model in cache!')
                break
            start_epoch = epoch

        if not model:
            if self.dm == 0:
                # PV-DBOW
                log_to_info('Yep, this is DBOW!')
                model = Doc2Vec(dm=self.dm, hs=0, workers=self.workers, size=self.mp.word_vector_dimensionality, min_count=self.min_count,
                                window=self.mp.word_context_window, sample=self.mp.frequent_words_downsampling_dbow, seed=random_int(),
                                negative=self.mp.negative)
                # model = Doc2Vec(dm=0, size=100, negative=5, hs=0, min_count=2, workers=8)
            elif self.dm == 1:
                # PV-DM w/average
                log_to_info('Yep, this is DM!')
                model = Doc2Vec(dm=self.dm, dm_mean=1, hs=0, workers=self.workers, size=self.mp.word_vector_dimensionality,
                                min_count=self.min_count, window=self.mp.word_context_window, sample=self.mp.frequent_words_downsampling_dm,
                                seed=random_int(), negative=self.mp.negative)
                # model = Doc2Vec(dm=1, dm_mean=1, size=100, window=10, negative=5, hs=0, min_count=2, workers=8)

            start1 = time.time()
            model.build_vocab(labeled_reviews)
            start1 = time.time()
            end1 = time.time()
            log_to_info('Vocab building for dm{0} took {1} seconds'.format(self.dm, end1 - start1))

        log_to_info('Training Doc2Vec model...')
        for epoch in range(start_epoch, self.epochs + 1):
            log_to_info('Epoch {0} of {1}'.format(epoch, self.epochs))
            m = self.load_model(epoch)
            if m is not None:
                log_to_info('Found model in cache!')
                model = m
                continue

            permuted_labeled_reviews = labeled_reviews[:]
            random.shuffle(permuted_labeled_reviews)

            alpha = alpha_for_epoch(epoch, self.mp.epochs_total, self.mp.alpha_max, self.mp.alpha_min, self.mp.learning_rate_type)
            model.min_alpha, model.alpha = alpha, alpha

            start2 = time.time()
            model.train(permuted_labeled_reviews)
            end2 = time.time()
            log_to_info('DM HPV is {0}, DBOW HPV is {1}'.format(self.mp.hierarchical_paragraph_vectors_dm,
                                                                self.mp.hierarchical_paragraph_vectors_dbow))
            log_to_info('Model training for dm{0} took {1} seconds'.format(self.dm, end2 - start2))

            self.model = model
            self.store_model(epoch)

        self.model = model
