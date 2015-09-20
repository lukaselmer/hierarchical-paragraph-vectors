from sklearn.linear_model import LogisticRegressionCV
import statsmodels
from helpers.log_config import log_to_info
import statsmodels.api as sm


class LogisticClassifier(object):
    def classify(self, mp, x_train, y_train, x_test):
        x_train = sm.add_constant(x_train)
        x_test = sm.add_constant(x_test)
        clf = LogisticRegressionCV(verbose=1, cv=5)
        log_to_info('Fitting a Logistic Regression to labeled training data...')
        clf = clf.fit(x_train, y_train)
        log_to_info('Training details')
        log_to_info('Classifier parameters: {}'.format(clf.get_params()))
        log_to_info('On training: {}'.format(clf.score(x_train, y_train) * 100.0))
        log_to_info('Predicting test value')
        y_test = clf.predict(x_test)
        log_to_info('Done!')
        return y_test


        # clf = LinearSVC(dual=False, verbose=True, C=mp.classifier_c, penalty=mp.classifier_penalty)  # C=0.00101
        # clf = SVC(gamma=2, C=1, verbose=True)
        # clf = LinearSVC(dual=False, verbose=True, C=1.0)
        # clf = LinearSVC(dual=False, verbose=True, C=1000.0)
        # clf = LinearSVC(dual=False, verbose=True, C=0.00101)
        # 88.2% clf = LinearSVC(dual=False, verbose=True, C=0.0195, penalty='l1') #C=0.00101
        # clf = LinearSVC(dual=False, verbose=True, C=0.0195, penalty='l1')  # C=0.00101
        # clf = LinearSVC(dual=False, verbose=True, C=0.0195, penalty='l1')
        # clf = LinearSVC(dual=True, verbose=True, C=0.005, loss='hinge')
        # clf = LinearSVC(dual=False, verbose=True, C=0.0005)
        # clf = LogisticRegression(penalty='l2', dual=True, tol=0.0001, C=1, fit_intercept=True, intercept_scaling=1.0, class_weight=None,
        #                         random_state=None)
        # clf = LogisticRegression(C=1.1)
        # log_to_info(len(x_train[0]))
        # log_to_info(y_train)
        # log_to_info(len(x_test[0]))
        # log_to_info(y_test)
        # Write the test results
        # return pd.DataFrame(data={'id': testing_data_ids, 'sentiment': y_test})
