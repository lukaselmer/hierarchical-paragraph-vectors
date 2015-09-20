import numpy
import statsmodels.api as sm
from helpers.log_config import log_to_info


class LogisticClassifier2(object):
    def classify(self, mp, x_train, y_train, x_test):
        x_train_reg = sm.add_constant(x_train)
        x_test_reg = sm.add_constant(x_test)
        logit =  sm.Logit(y_train, x_train_reg)
        clf = logit.fit(disp=0)
        # print(clf.summary())
        log_to_info('Fitting a Logistic Regression to labeled training data...')
        log_to_info('Predicting test value')
        y_test = clf.predict(x_test_reg)
        log_to_info('Done!')

        return numpy.rint(y_test)
