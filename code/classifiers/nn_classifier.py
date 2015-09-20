import numpy as np
from sknn.mlp import Regressor, Layer

from helpers.log_config import log_to_info


class NNClassifier(object):
    def classify(self, x_train, y_train, x_test):
        x_train = np.array(x_train)
        y_train = np.array(y_train)
        x_test = np.array(x_test)
        # nn = Classifier(
        #    layers=[
        #        Layer("Maxout", units=100, pieces=2),
        #        Layer("Softmax")],
        #    learning_rate=0.001,
        #    n_iter=25)
        # nn.fit(x_train, y_train)
        # y_test = nn.predict(np.array(x_test))

        nn = Regressor(layers=[Layer('Rectifier', units=400), Layer('Linear')], learning_rate=0.02, n_iter=10)
        log_to_info('Fitting a NN to labeled training data...')
        nn.fit(np.array(x_train), np.array(y_train))
        log_to_info('Predicting test value')
        y_test = nn.predict(np.array(x_test))
        log_to_info('Done!')

        return y_test
