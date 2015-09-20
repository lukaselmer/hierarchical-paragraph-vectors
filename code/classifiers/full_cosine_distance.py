import numpy as np
from sklearn.metrics import pairwise_distances


class FullCosineDistanceClassifier(object):
    # cosine 70%
    # cosine 70%
    def classify(self, x_train, y_train, x_test, distance):
        # y_test = np.zeros(len(y_test_reviews))

        # features: 1000
        # j = (1...2187)
        # x_train shape: (22813, 1000)
        # x_test shape: (2187, 1000)
        # y_train shape: (22813, 1)
        # y_train_centered shape: (22813, 1)
        # z shape: (22813, 2187)
        # num shape: (2187,0)
        # de_num shape: (2187,0)

        y_train_centered = np.add(np.array(y_train), -0.5) * -1

        z = pairwise_distances(x_train, x_test, distance)
        # z = np.exp(z)

        num = np.sum(z, axis=0)
        de_num = np.dot(z.T, y_train_centered)
        tot = np.divide(num, de_num)
        y_test = (np.sign(tot) + 1) / 2

        return y_test
