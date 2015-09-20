import numpy
from helpers.d2v_identifier_helper import get_d2v_identifier


def convert_to_vector(d2v_id, model_dm, model_dbow):
    d2v_identifier = get_d2v_identifier(d2v_id)
    a = extract_vector_from_model(d2v_identifier, model_dm)
    b = extract_vector_from_model(d2v_identifier, model_dbow)
    if a is None or b is None:
        raise 'a or b is none! {}'.format(d2v_identifier)

    return numpy.concatenate([a, b])


def extract_vector_from_model(d2v_identifier, model_dm):
    if hasattr(model_dm, 'docvecs'):
        if d2v_identifier not in model_dm.docvecs:
            return None
        return model_dm.docvecs[d2v_identifier]

    if d2v_identifier not in model_dm.vocab:
        return None
    return model_dm[d2v_identifier]
