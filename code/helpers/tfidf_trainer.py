import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from helpers.log_config import log_to_info


def train_tfidf_vectors(mp, testing_reviews, training_reviews, x_train, x_test):
    log_to_info('Training tfid vectors')
    tfv = TfidfVectorizer(max_features=mp.tfid_features)
    tr = list(training_reviews['words'].values)
    te = list(testing_reviews['words'].values)
    space_separated_words = tr + te
    tfid_vectors = tfv.fit_transform(space_separated_words)
    x_train_tfid = tfid_vectors[:len(tr)].toarray()
    x_test_tfid = tfid_vectors[len(tr):].toarray()

    if x_train is None:
        x_train = x_train_tfid
        x_test = x_test_tfid
    else:
        x_train = np.concatenate([np.array(list(x_train)), x_train_tfid], axis=1)
        x_test = np.concatenate([np.array(list(x_test)), x_test_tfid], axis=1)

    return x_train, x_test
