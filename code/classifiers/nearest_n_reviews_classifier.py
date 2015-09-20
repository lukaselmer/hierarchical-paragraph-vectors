import numpy as np
from helpers.d2v_identifier_helper import get_d2v_identifier

from helpers.log_config import log_to_info


class NearestNReviewsClassifier(object):
    # nearest_reviews_count=1: 55%
    # nearest_reviews_count=100: 60%
    # nearest_reviews_count=500: 66%
    # nearest_reviews_count=1000: 67.9%
    # nearest_reviews_count=1500: 68.7%
    # nearest_reviews_count=2000: 69.5%
    def classify(self, model, y_test_reviews, reviews, nearest_reviews_count=2000):
        y_test = np.zeros(len(y_test_reviews))

        i = 0
        for d2v_numeric_id in y_test_reviews['d2v_id']:
            if i % 100 == 0:
                log_to_info('Processing {0} of {1} ({2}%)'.format(i, len(y_test_reviews), 1.0 * i / len(y_test_reviews) * 100.0))
            d2v_id = get_d2v_identifier(d2v_numeric_id)
            arr = model.most_similar(d2v_id, topn=10000)
            sentiment_sum = 0.0
            total_neareness = 0.0
            total_sentiments = 0
            for key in arr:
                if key[0].startswith('REVIEW_'):
                    most_similar_review = key[0]
                    most_similar_id = int(most_similar_review.split('_')[1])
                    r = reviews[reviews['d2v_id'].eq(most_similar_id)]
                    if r['use_for_classifier_training'].all():
                        sentiment = r['sentiment'].values[0]
                        nearness = key[1]
                        sentiment_sum += sentiment * nearness
                        total_neareness += nearness
                        total_sentiments += 1
                        if total_sentiments >= nearest_reviews_count:
                            break
            # log_to_info('{0} predicts {1}'.format(d2v_id, sentiment))

            if total_neareness == 0:
                log_to_info('key {0} has no similar review!'.format(d2v_id))
                y_test[i] = 0
            else:
                sentiment = 0 if sentiment_sum <= total_neareness * 0.5 else 1
                y_test[i] = sentiment

            i += 1

        return y_test
