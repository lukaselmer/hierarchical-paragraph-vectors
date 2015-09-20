from helpers.log_config import log_to_info


def start_manual_run(func):
    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=16, frequent_words_downsampling=1e-4, negative=17,
    #      hierarchical_paragraph_vectors=0, epochs=3, epochs_total=3, classifier_name='rbf', classifier_c=0.0195, classifier_penalty='l2',
    #      tfid_features=0, learning_rate_type='linear')
    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=16, frequent_words_downsampling=1e-4, negative=17,
    #      hierarchical_paragraph_vectors=0, epochs=2, epochs_total=3, classifier_name='rbf', classifier_c=0.0195, classifier_penalty='l2',
    #      tfid_features=0, learning_rate_type='linear')
    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=16, frequent_words_downsampling=1e-4, negative=17,
    #      hierarchical_paragraph_vectors=0, epochs=1, epochs_total=3, classifier_name='rbf', classifier_c=0.0195, classifier_penalty='l2',
    #      tfid_features=0, learning_rate_type='linear')

    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=16, frequent_words_downsampling=1e-4, negative=17,
    #      hierarchical_paragraph_vectors=0, epochs=20, epochs_total=20, classifier_name='rbf', classifier_c=0.0195, classifier_penalty='l2',
    #      tfid_features=0, learning_rate_type='linear')
    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=16, frequent_words_downsampling=1e-4, negative=17,
    #      hierarchical_paragraph_vectors=0, epochs=15, epochs_total=20, classifier_name='rbf', classifier_c=0.0195, classifier_penalty='l2',
    #      tfid_features=0, learning_rate_type='linear')
    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=16, frequent_words_downsampling=1e-4, negative=17,
    #      hierarchical_paragraph_vectors=0, epochs=10, epochs_total=20, classifier_name='rbf', classifier_c=0.0195, classifier_penalty='l2',
    #      tfid_features=0, learning_rate_type='linear')
    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=16, frequent_words_downsampling=1e-4, negative=17,
    #      hierarchical_paragraph_vectors=0, epochs=5, epochs_total=20, classifier_name='rbf', classifier_c=0.0195, classifier_penalty='l2',
    #      tfid_features=0, learning_rate_type='linear')
    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=16, frequent_words_downsampling=1e-4, negative=17,
    #      hierarchical_paragraph_vectors=0, epochs=4, epochs_total=20, classifier_name='rbf', classifier_c=0.0195, classifier_penalty='l2',
    #      tfid_features=0, learning_rate_type='linear')
    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=16, frequent_words_downsampling=1e-4, negative=17,
    #      hierarchical_paragraph_vectors=0, epochs=3, epochs_total=20, classifier_name='rbf', classifier_c=0.0195, classifier_penalty='l2',
    #      tfid_features=0, learning_rate_type='linear')
    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=16, frequent_words_downsampling=1e-4, negative=17,
    #      hierarchical_paragraph_vectors=0, epochs=2, epochs_total=20, classifier_name='rbf', classifier_c=0.0195, classifier_penalty='l2',
    #      tfid_features=0, learning_rate_type='linear')
    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=16, frequent_words_downsampling=1e-4, negative=17,
    #      hierarchical_paragraph_vectors=0, epochs=1, epochs_total=20, classifier_name='rbf', classifier_c=0.0195, classifier_penalty='l2',
    #      tfid_features=0, learning_rate_type='linear')

    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=16, frequent_words_downsampling=1e-4, negative=17,
    #      hierarchical_paragraph_vectors=0, epochs=3, epochs_total=3, classifier_name='rbf', classifier_c=0.0195, classifier_penalty='l2',
    #      tfid_features=0, learning_rate_type='exp')
    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=16, frequent_words_downsampling=1e-4, negative=17,
    #      hierarchical_paragraph_vectors=0, epochs=2, epochs_total=3, classifier_name='rbf', classifier_c=0.0195, classifier_penalty='l2',
    #      tfid_features=0, learning_rate_type='exp')
    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=16, frequent_words_downsampling=1e-4, negative=17,
    #      hierarchical_paragraph_vectors=0, epochs=1, epochs_total=3, classifier_name='rbf', classifier_c=0.0195, classifier_penalty='l2',
    #      tfid_features=0, learning_rate_type='exp')

    # run_and_say(algorithm_version=3, word_vector_dimensionality=48, word_context_window=10, frequent_words_downsampling=1e-4,
    # negative=17, hierarchical_paragraph_vectors=1, epochs=1, classifier_name='rbf')

    version = 77.8
    # epochs = list(range(1, 5)) + list(range(5, 76, 5))
    epochs = list(range(1, 6))
    # for epoch in epochs:
    # log_to_info('Epoch exp: {}'.format(epoch))
    # func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=10, frequent_words_downsampling=0, negative=5,
    #      hierarchical_paragraph_vectors=0, epochs=epoch, epochs_total=max(epochs), classifier_name='rbf', classifier_c=0.0195,
    #      classifier_penalty='l2', tfid_features=0, learning_rate_type='exp')
    # log_to_info('Epoch was exp: {}'.format(epoch))
    epochs = [3]
    epoch = max(epochs)
    log_to_info('Epoch linear: {}'.format(epoch))
    hpv = 0
    func(algorithm_version=version, word_vector_dimensionality=48, word_context_window=10, frequent_words_downsampling_dm=0.0001,
         frequent_words_downsampling_dbow=0.01, negative=25, hierarchical_paragraph_vectors=hpv, epochs=epoch, epochs_total=max(epochs),
         classifier_name='svc', classifier_c=0.0195, classifier_penalty='l2', tfid_features=0, learning_rate_type='exp',
         experiment_number=1)
    # func(algorithm_version=version, word_vector_dimensionality=100, word_context_window=10, frequent_words_downsampling=0, negative=5,
    #     hierarchical_paragraph_vectors=5, epochs=epoch, epochs_total=max(epochs), classifier_name='svc', classifier_c=0.0195,
    #     classifier_penalty='l2', tfid_features=0, learning_rate_type='linear')
    log_to_info('Epoch was linear: {}'.format(epoch))

    # log_to_info('Epoch linear: {}'.format(epoch))
    # func(algorithm_version=version, word_vector_dimensionality=100, word_context_window=10, frequent_words_downsampling=0, negative=5,
    #     hierarchical_paragraph_vectors=4, epochs=epoch, epochs_total=max(epochs), classifier_name='svc', classifier_c=0.0195,
    #     classifier_penalty='l2', tfid_features=0, learning_rate_type='linear')
    # log_to_info('Epoch was linear hpv 4: {}'.format(epoch))
