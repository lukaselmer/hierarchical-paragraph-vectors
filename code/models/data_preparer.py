import os
import gensim

import pandas
import re

from helpers.data_path import cache_path, data_path, csv_extension, use_different_source
from helpers.kaggle_word2vec_utility import KaggleWord2VecUtility


def sentiment_from_id(review_id):
    """
    :type review_id: str
    """
    a, rating_str = review_id.replace('"', '').split('_')
    rating = int(rating_str)
    return 1 if rating >= 5 else 0


class DataPreparer:
    def __init__(self, mp):
        self.mp = mp

    def convert(self):
        return self._convert_to_export()

    def save_reviews_with_topics(self, reviews):
        destination = cache_path('{}{}.hdf'.format(self.mp.preprocessing_name(), csv_extension()))
        reviews.to_hdf(destination, 'export', mode='w')

    def _convert_to_export(self):
        destination = cache_path('{}{}.hdf'.format(self.mp.preprocessing_name(), csv_extension()))
        if os.path.exists(destination):
            return pandas.read_hdf(destination, 'export')

        training_data = self._training_data().copy()
        training_data['use_for_classifier_training'] = True
        training_data['use_for_score_calculation'] = False
        training_data['predict_sentiment'] = False
        training_data['predicted_sentiment'] = None

        unlabeled_training_data = self._unlabeled_training_data().copy()
        unlabeled_training_data['use_for_classifier_training'] = False
        unlabeled_training_data['use_for_score_calculation'] = False
        unlabeled_training_data['sentiment'] = None
        unlabeled_training_data['predict_sentiment'] = False
        unlabeled_training_data['predicted_sentiment'] = None

        if not use_different_source():
            self._preprocess_test_data()
        testing_data = self._testing_data()
        testing_data['use_for_classifier_training'] = False
        testing_data['use_for_score_calculation'] = True
        testing_data['predict_sentiment'] = True
        testing_data['predicted_sentiment'] = None

        reviews = self._post_process([training_data, unlabeled_training_data, testing_data])
        reviews.to_hdf(destination, 'export', mode='w')
        return reviews

    def _post_process(self, raw_data):
        reviews = pandas.concat(raw_data)
        reviews = reviews.reset_index(drop=True)
        reviews['d2v_id'] = reviews.index
        reviews['predicted_sentiment'] = None

        def convert_review_to_words(review_str):
            return ' '.join(KaggleWord2VecUtility.review_to_word_list(review_str))

        reviews['words'] = reviews['review'].apply(convert_review_to_words)

        return reviews

    def _load_all_data(self, review_group):
        all_docs = dict(training=[], testing=[], unlabeled=[])
        with open(data_path('alldata-id.txt')) as lines:
            for line_no, line in enumerate(lines):
                tokens = gensim.utils.to_unicode(line).split()
                review_id = line_no + 1
                words = tokens[1:]
                split = ['training', 'testing', 'unlabeled', 'unlabeled'][line_no // 25000]
                sentiment = [1, 0, 1, 0, 0, 0, 0, 0][line_no // 12500]
                all_docs[split].append(dict(id=review_id, sentiment=sentiment, review=' '.join(words)))
        ret = pandas.DataFrame(all_docs[review_group])
        return ret

    def _training_data(self):
        if use_different_source():
            return self._load_all_data('training')
        return self._load_data('labeledTrainData{}'.format(csv_extension()))

    def _testing_data(self):
        if use_different_source():
            return self._load_all_data('testing')
        return self._load_data('cheatTestData{}'.format(csv_extension()))

    def _unlabeled_training_data(self):
        if use_different_source():
            return self._load_all_data('unlabeled')
        return self._load_data('unlabeledTrainData{}'.format(csv_extension()))

    def _load_data(self, filename):
        return pandas.read_csv(data_path(filename), header=0)

    def _preprocess_test_data(self):
        cheat_path = data_path('cheatTestData{}'.format(csv_extension()))
        if os.path.isfile(cheat_path):
            return

        test_data = self._load_data('testData{}'.format(csv_extension()))
        test_data['sentiment'] = test_data['id'].map(sentiment_from_id)
        test_data.to_csv(cheat_path, index=False, header=True)
