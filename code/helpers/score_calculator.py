import numpy
from helpers.log_config import log_to_info


class ScoreCalculator(object):
    def print_score(self, reviews):
        score, correct, total = self.calculate_score(reviews)
        log_to_info('Score: {0}%, which is {1}/{2}'.format(score, correct, total))

    def calculate_score(self, reviews):
        reviews_for_score_calculation = reviews[reviews['use_for_score_calculation'].eq(True)]

        wrong = reviews_for_score_calculation['sentiment'] - reviews_for_score_calculation['predicted_sentiment']
        wrong_results = wrong.apply(abs).sum()

        total = len(reviews_for_score_calculation)
        correct = total - wrong_results
        return 100.0 * correct / total, correct, total
