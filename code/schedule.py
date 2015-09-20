from helpers.api import schedule_runs


def schedule_main():
    algorithm_version = 16.0
    epochs = list(range(1, 11))
    epochs_total = 10

    general_params = dict(algorithm_version=[algorithm_version], word_vector_dimensionality=[200], word_context_window=[10],
                          frequent_words_downsampling_dm=[0.0001], frequent_words_downsampling_dbow=[0.01], negative=[25],
                          hierarchical_paragraph_vectors=[0, 4], epochs_total=[epochs_total], learning_rate_type=['exp'],
                          experiment_number=[1])
    narrow_params = dict(epochs=epochs, classifier_name=['svc'], classifier_c=[0.0195], classifier_penalty=['l2'], tfid_features=[0])

    schedule_runs(general_params, narrow_params)


if __name__ == '__main__':
    schedule_main()
