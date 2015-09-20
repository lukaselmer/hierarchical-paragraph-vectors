from classifiers.linear_svc_classifier import LinearSVCClassifier
from classifiers.logistic_classifier import LogisticClassifier
from classifiers.logistic_classifier2 import LogisticClassifier2
from classifiers.rbf_classifier import RbfClassifier
from classifiers.rbf_svc_classifier import RbfSVCClassifier
from helpers.log_config import log_to_info


def classify(mp, x_test, x_train, y_train):
    log_to_info('Starting classification')
    classifiers = dict(logistic=LogisticClassifier, logistic2=LogisticClassifier2, rbf=RbfClassifier, rbf_scv=RbfSVCClassifier,
                       svc=LinearSVCClassifier)
    return classifiers[mp.classifier_name]().classify(mp, x_train, y_train, x_test)
