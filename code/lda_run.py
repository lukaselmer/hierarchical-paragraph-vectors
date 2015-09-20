import os
import time
import gensim
from gensim.interfaces import TransformedCorpus
from nltk.corpus import stopwords
from helpers.log_config import setup_logger, log_to_info
from helpers.random_helper import init_random
from models.data_preparer import DataPreparer
from models.model_parameters import ModelParameters

num_topics = 50
model_type = 'lda'
mm_cache_name = 'model_data/lda_dictionary_nostops2.mm'
dictionary_cache_name = 'model_data/lda_dictionary_nostops2.dict'
single_pass = False
lda_cache_name = 'model_data/{}-nostops2-topics.{}'.format(num_topics, model_type)


def extract_topics(topics_probabilities):
    sorted_topics = sorted(topics_probabilities, key=lambda top_prob: -top_prob[1])
    best_topic = sorted_topics[0][0] if len(sorted_topics) > 0 else None
    second_best_topic = sorted_topics[1][0] if len(sorted_topics) > 1 else None
    return [best_topic, second_best_topic]


def infer_topics(lda, reviews):
    print('inferring...')
    # documents = _get_documents()
    # dictionary = gensim.corpora.Dictionary.load(dictionary_cache_name)
    # query = dictionary.doc2bow(documents[0])
    # print(lda[query])
    return
    corpus = gensim.corpora.MmCorpus(mm_cache_name)
    res = lda.get_document_topics(corpus, 0.25)

    print('done, now the loop...')
    all_best_topics = map(extract_topics, res)
    print('done with the loop')
    best_topics, second_best_topics = zip(*all_best_topics)
    print('done with zipping')
    data_preparer = _get_data_preparer()
    reviews['best_topics'] = best_topics
    reviews['second_best_topics'] = second_best_topics
    print('saving new reviews')
    data_preparer.save_reviews_with_topics(reviews)
    print('done!')


def main():
    setup_logger()
    init_random()
    log_to_info('starting main')
    start = time.time()

    reviews = _get_reviews()
    if 'best_topics' in reviews:
        log_to_info('best topics already set, aborting!')
        return

    log_to_info('getting reviews done')

    if not os.path.exists(dictionary_cache_name) or not os.path.exists(mm_cache_name):
        documents = _get_documents(reviews)

    log_to_info('dictionary')

    if os.path.exists(dictionary_cache_name):
        dictionary = gensim.corpora.Dictionary.load(dictionary_cache_name)
    else:
        dictionary = gensim.corpora.Dictionary(documents)
        dictionary.save(dictionary_cache_name)

    log_to_info('mm')
    if os.path.exists(mm_cache_name):
        corpus = gensim.corpora.MmCorpus(mm_cache_name)
    else:
        corpus = [dictionary.doc2bow(text) for text in documents]
        gensim.corpora.MmCorpus.serialize(mm_cache_name, corpus)

    log_to_info('lda')
    if os.path.exists(lda_cache_name):
        if model_type == 'lsi':
            lda = gensim.models.LsiModel.load(lda_cache_name)
        else:
            lda = gensim.models.LdaModel.load(lda_cache_name)
    else:
        if model_type == 'lsi':
            lda = gensim.models.LsiModel(corpus=corpus, id2word=dictionary, num_topics=num_topics)
        elif single_pass:
            lda = gensim.models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=20)
        else:
            lda = gensim.models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=20, update_every=0, passes=20)
        lda.save(lda_cache_name)

    log_to_info('it took {0} seconds'.format(time.time() - start))
    infer_topics(lda, reviews)
    log_to_info('everything took {0} seconds'.format(time.time() - start))

    # training_reviews = reviews[reviews['use_for_classifier_training'].eq(True)]


def _get_documents(reviews):
    print('getting the documents...')
    reviews_list_words = list(reviews['words'])
    documents = []
    stops = set(stopwords.words('english')).union(set('exspec7 sentspecl0 sentspecl1 specialcharaps specialparachardbr specsingl10 '
                                                      'specsingl3 specsingl4 subsentspecl0 subsentspecl1 subsentspeclbra0'.split(' ')))
    for space_separated_words in reviews_list_words:
        space_separated_words = space_separated_words.replace(' paragraphend', '')
        space_separated_words = space_separated_words.replace(' sentenceend', '')
        space_separated_words = space_separated_words.replace(' subsentenceend', '')
        documents.append([w for w in space_separated_words.split(' ') if w not in stops])
    return documents


def _get_reviews():
    data_preparer = _get_data_preparer()
    reviews = data_preparer.convert()
    return reviews


def _get_data_preparer():
    mp = ModelParameters(algorithm_version=77.77, word_vector_dimensionality=400, word_context_window=10, frequent_words_downsampling=0,
                         negative=5, hierarchical_paragraph_vectors=0, epochs=1, epochs_total=1, classifier_name='svc', classifier_c=0.0195,
                         classifier_penalty='l2', tfid_features=0, learning_rate_type='linear')
    data_preparer = DataPreparer(mp)
    return data_preparer


if __name__ == '__main__':
    main()
