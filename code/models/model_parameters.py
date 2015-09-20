class ModelParameters:
    def __init__(self, algorithm_version, word_vector_dimensionality, word_context_window, frequent_words_downsampling_dm,
                 frequent_words_downsampling_dbow, negative, epochs, epochs_total, classifier_name, classifier_c, classifier_penalty,
                 tfid_features, learning_rate_type, experiment_number, hierarchical_paragraph_vectors):
        # word2vec params
        self.algorithm_version = algorithm_version
        self.frequent_words_downsampling_dm = frequent_words_downsampling_dm
        self.frequent_words_downsampling_dbow = frequent_words_downsampling_dbow
        self.hierarchical_paragraph_vectors = hierarchical_paragraph_vectors

        if '/' in str(hierarchical_paragraph_vectors):
            self.hierarchical_paragraph_vectors_dm, self.hierarchical_paragraph_vectors_dbow = map(int, hierarchical_paragraph_vectors.split('/'))
        else:
            self.hierarchical_paragraph_vectors_dm = self.hierarchical_paragraph_vectors_dbow = hierarchical_paragraph_vectors

        self.word_vector_dimensionality = word_vector_dimensionality
        self.word_context_window = word_context_window
        self.negative = negative
        self.epochs = epochs

        self.epochs_total = epochs_total
        self.alpha_min = 0.001
        self.alpha_max = 0.025
        self.min_count = 2
        self.learning_rate_type = learning_rate_type
        self.experiment_number = experiment_number

        # classifier params
        self.classifier_name = classifier_name
        self.classifier_c = classifier_c
        self.classifier_penalty = classifier_penalty
        self.tfid_features = tfid_features

    def preprocessing_name(self):
        return 'data-export-new.hdf'

    def word2vec_model_path(self, epoch=None):
        params = dict(fwd=self.frequent_words_downsampling_dm, fwc=self.frequent_words_downsampling_dbow,
                      wvd=self.word_vector_dimensionality, wcw=self.word_context_window, neg=self.negative,
                      hpv=self.hierarchical_paragraph_vectors, ept=self.epochs_total, ami=self.alpha_min, ama=self.alpha_max,
                      lrt=self.learning_rate_type, mic=self.min_count, exn=self.experiment_number)
        directory_name = '-'.join(sorted(['{}{}'.format(k, params[k]) for k in params if params[k]]))

        real_epochs = self.epochs if epoch is None else epoch

        return 'v{}/{}/epo{}'.format(self.algorithm_version, directory_name, real_epochs)
