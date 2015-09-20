from sklearn import pipeline, cross_validation
from sklearn.kernel_approximation import Nystroem
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.utils.multiclass import type_of_target

from helpers.log_config import log_to_info


class LinearSVCClassifier(object):
    def classify(self, mp, x_train, y_train, x_test):
        clf = LinearSVC(dual=False, verbose=False, C=1.0)
        log_to_info('Fitting a LinearSVC to labeled training data...')
        clf = clf.fit(x_train, y_train)
        log_to_info('Predicting test value')
        y_test = clf.predict(x_test)
        log_to_info('Done!')

        return y_test
