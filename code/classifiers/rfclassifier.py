import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from helpers.log_config import log_to_info


class RFClassifier(object):
    def classify(self, mp, train_centroids, training_data_sentiment, test_centroids, testing_data_ids):
        # ****** Fit a random forest and extract predictions
        clf = RandomForestClassifier(n_estimators=mp.random_forest_estimators)

        # Fitting the forest may take a few minutes
        log_to_info('Fitting a random forest to labeled training data...')
        clf = clf.fit(train_centroids, training_data_sentiment)
        result = clf.predict(test_centroids)

        # Write the test results
        return pd.DataFrame(data={'id': testing_data_ids, 'sentiment': result})
