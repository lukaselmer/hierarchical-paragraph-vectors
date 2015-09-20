use_tags = False
try:
    from gensim.models.doc2vec import TaggedDocument

    use_tags = True
except ImportError:
    from gensim.models.doc2vec import LabeledSentence


def create_tagged_document(tags, words):
    if use_tags:
        return TaggedDocument(words=words, tags=tags)
    else:
        return LabeledSentence(words=words, labels=tags)


def save_doc2vec_model(model, model_path):
    if use_tags:
        model.save(model_path, pickle_protocol=3)
    else:
        model.save(model_path)
