from sklearn import pipeline, cross_validation
from sklearn.kernel_approximation import Nystroem
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.utils.multiclass import type_of_target

from helpers.log_config import log_to_info


class RbfClassifier(object):
    def classify(self, mp, x_train, y_train, x_test):
        feature_map_nystroem = Nystroem(random_state=1, gamma=1.1, n_components=1000)  # gamma=0.00005,
        clf = pipeline.Pipeline([("feature_map", feature_map_nystroem), ("svm", LinearSVC())])
        log_to_info('Fitting a RBF SVM to labeled training data...')
        clf = clf.fit(x_train, y_train)
        log_to_info('Predicting test value')
        y_test = clf.predict(x_test)
        log_to_info('Done!')

        return y_test

        # y_train = list(y_train.values)
        # scaler = preprocessing.StandardScaler().fit(x_train)
        # scaler = preprocessing.MinMaxScaler().fit(x_train)
        # scaler = preprocessing.Normalizer().fit(x_train)
        # x_train = scaler.transform(x_train)
        # x_test = scaler.transform(x_test)
        # scaler = preprocessing.Binarizer(threshold=0.01).fit(x_train)
        # scaler = preprocessing.Normalizer().fit(x_train)
        # x_train = scaler.transform(x_train)
        # x_test = scaler.transform(x_test)


        # ****** Fit a random forest and extract predictions
        # clf = SVC(gamma=2, C=1, verbose=True)

        # scaler = preprocessing.StandardScaler().fit(x_train)
        # x_train = scaler.transform(x_train)
        # x_test = scaler.transform(x_test)

        # rbf = RBFSampler(gamma=.2, random_state=1)
        # y_train = training_data_sentiment
        # x_train = rbf.fit_transform(train_centroids)
        # x_test = rbf.transform(test_centroids)

        # 84.56% feature_map_fourier = RBFSampler(gamma=0.0001, random_state=1, n_components=2000)
        # 85.16% feature_map_fourier = RBFSampler(gamma=0.0002, random_state=1, n_components=2000)
        # 84.92% feature_map_fourier = RBFSampler(gamma=0.0002, random_state=1, n_components=2500)
        # 84.48% feature_map_fourier = RBFSampler(gamma=0.0005, random_state=1, n_components=2000)
        # feature_map_fourier = RBFSampler(gamma=0.001, random_state=1, n_components=300)
        # clf = pipeline.Pipeline([("feature_map", feature_map_fourier), ("svm", LinearSVC())])
        # clf.set_params(feature_map__n_components=2000)

        # new 79.8353909465% feature_map_nystroem = Nystroem(random_state=1, gamma=1.1, n_components=1000)  # gamma=0.00005,
        # feature_map_nystroem = Nystroem(random_state=1, gamma=0.00001, n_components=1500)  # gamma=0.00005,
        # 86.48% feature_map_nystroem = Nystroem(random_state=1, gamma=0.0001, n_components=1500)  # gamma=0.00005,
        # 87.32% feature_map_nystroem = Nystroem(random_state=1, gamma=0.0005, n_components=1500)  # gamma=0.00005,
        # 87.28% feature_map_nystroem = Nystroem(random_state=1, gamma=0.0005, n_components=1700)
        # feature_map_nystroem = Nystroem(kernel='sigmoid', random_state=1, gamma=0.001, n_components=2800)  # gamma=0.00005,
        # xxxxx% feature_map_nystroem = Nystroem(kernel='chi2', random_state=1, gamma=0.001, n_components=1000)  # gamma=0.00005,

        # x_train2 = np.zeros((len(x_train), len(x_train[0])), dtype='float32')
        # x_test2 = np.zeros((len(x_test), len(x_test[0])), dtype='float32')
        # counter = 0
        # for x in x_train:
        #     z = np.zeros(len(x), dtype='float32')
        #     zcounter = 0
        #     for zz in x:
        #         z[zcounter] = zz
        #         zcounter += 1
        #     x_train2[counter] = z
        #     counter += 1
        # counter = 0
        # for x in x_test:
        #     z = np.zeros(len(x), dtype='float32')
        #     zcounter = 0
        #     for zz in x:
        #         z[zcounter] = zz
        #         zcounter += 1
        #     x_test2[counter] = z
        #     counter += 1
        # x_train = x_train2
        # x_test = x_test2
        #
        # log_to_info(x_test)

        # print cross_validation.cross_val_score(clf, x_train, y_train, cv=20, scoring='roc_auc')

        # clf = LinearSVC(dual=False, verbose=True, C=1.0)
        # clf = LinearSVC(dual=False, verbose=True, C=1000.0)
        # clf = LinearSVC(dual=False, verbose=True, C=0.00101)
        # 88.2% clf = LinearSVC(dual=False, verbose=True, C=0.0195, penalty='l1') #C=0.00101
        # clf = LinearSVC(dual=False, verbose=True, C=0.0195, penalty='l1')
        # clf = LinearSVC(dual=True, verbose=True, C=0.005, loss='hinge')
        # clf = LinearSVC(dual=False, verbose=True, C=0.0005)
        # direct: 79.1952446273% clf = LinearSVC(dual=False, verbose=True, C=1.0)
        # clf = LinearSVC(dual=False, verbose=True, C=1.0)
        # clf = LinearSVC(dual=True, verbose=True, loss='hinge', C=1.0)
