#!/usr/bin/env python

import time
from algorithms.manual_run import start_manual_run

from helpers.classification_helper import classify
from helpers.d2v_extraction_helper import convert_to_vector
from helpers.data_path import check_paths_and_create_directories
from helpers.log_config import log_to_info, setup_logger
from helpers.random_helper import init_random
from helpers.result_extraction import say_result
from helpers.score_calculator import ScoreCalculator
from helpers.tfidf_trainer import train_tfidf_vectors
from models.data_preparer import DataPreparer
from models.doc2vec_factory import Doc2VecFactory
from models.model_parameters import ModelParameters


def main(run=None):
    init_random()
    log_to_info('starting main')

    if run:
        slave_options = run['algo_params']
        run_with(**slave_options)
    else:
        start_manual_run(run_and_say)


def run_and_say(**kwargs):
    log_handler, log_buffer = setup_logger(True)
    run_with(**kwargs)
    say_result(log_handler, log_buffer)


def run_with(**kwargs):
    log_to_info(str(kwargs))
    check_paths_and_create_directories()
    start = time.time()
    mp = ModelParameters(**kwargs)

    reviews = DataPreparer(mp).convert()
    x_train, y_train, x_test = build_train_and_test_x(mp, reviews)

    y_test_reviews = reviews[reviews['predict_sentiment'].eq(True)].copy()
    y_test_reviews['predicted_sentiment'] = classify(mp, x_test, x_train, y_train)
    log_to_info(str(kwargs))
    ScoreCalculator().print_score(y_test_reviews)
    end = time.time()
    log_to_info('It took {0} seconds'.format(end - start))


def build_train_and_test_x(mp, reviews):
    log_to_info('Starting to load data')

    training_reviews = reviews[reviews['use_for_classifier_training'].eq(True)]
    testing_reviews = reviews[reviews['predict_sentiment'].eq(True)]

    x_train = None
    x_test = None

    if mp.word_vector_dimensionality:
        log_to_info('Starting to load the doc2vec model')
        model_dm = Doc2VecFactory(mp, reviews, 1).get_word2vec_model()
        model_dbow = Doc2VecFactory(mp, reviews, 0).get_word2vec_model()

        x_train = training_reviews['d2v_id'].map(lambda d2v_id: convert_to_vector(d2v_id, model_dm, model_dbow)).values
        x_test = testing_reviews['d2v_id'].map(lambda d2v_id: convert_to_vector(d2v_id, model_dm, model_dbow)).values

    if mp.tfid_features:
        x_train, x_test = train_tfidf_vectors(mp, testing_reviews, training_reviews, x_train, x_test)

    y_train = list(training_reviews['sentiment'].values)
    return list(x_train), y_train, list(x_test)
