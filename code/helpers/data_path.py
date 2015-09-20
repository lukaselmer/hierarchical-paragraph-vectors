from __future__ import with_statement
import os
from threading import Lock

import numpy as np
import pandas

from helpers.log_config import log_to_info

result_lock = Lock()


def _project_path():
    return os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), '..'))


def force_exists(path):
    if not os.path.exists(path):
        log_to_info('The file {0} does not exist!'.format(path))
        exit(1)


def use_different_source():
    return False


def csv_extension():
    if use_different_source():
        return 'DifferentSource.csv'
    return 'Converted3.csv'
    # return 'Converted2.csv'
    # return 'Clean.csv'


def check_paths_and_create_directories():
    # for x in ['labeledTrainData{}'.format(csv_extension()), 'testData{}'.format(csv_extension()),
    #       'unlabeledTrainData{}'.format(csv_extension())]:
    # force_exists(data_path(x))

    if not os.path.exists(cache_path('')):
        os.makedirs(cache_path(''))

    if not os.path.exists(_raw_results_path('')):
        os.makedirs(_raw_results_path(''))


def data_path(filename):
    return os.path.join(_project_path(), 'data', filename)


def cache_path(filename):
    return os.path.join(_project_path(), 'model_data', 'cache', filename)


def model_data_path(model_name):
    return os.path.join(_project_path(), 'model_data', model_name)


def _results_path(name):
    return os.path.join(_project_path(), 'results', name)


def _raw_results_path(name):
    return os.path.join(_project_path(), 'results', 'raw', name)


def store_np_data(name, data):
    np.save(model_data_path(name), data)
    return data


def check_np_data_cache(name):
    return os.path.isfile(model_data_path('{0}.npy'.format(name)))


def load_np_data(name):
    return np.load(model_data_path('{0}.npy'.format(name)))


def store_result(name, accuracy, seconds):
    data = dict(name=name, accuracy=accuracy, seconds=seconds)
    pandas.DataFrame(data, index=[0]).to_csv(_raw_results_path('{0}-{1}-{2}.csv'.format(accuracy, name, seconds)), index=False, quoting=3)
    with result_lock:
        accuracies = pandas.read_csv(_results_path('all.csv'), header=0, delimiter=',', quoting=3)
        new_accuracies = accuracies.append([data])
        new_accuracies.to_csv(_results_path('all.csv'), index=False, quoting=3)
