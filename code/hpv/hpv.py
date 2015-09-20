from helpers.d2v_identifier_helper import get_d2v_identifier
from helpers.gensim_version_abstraction import create_tagged_document


def convert_to_labeled_review(hpv_version, space_separated_words, d2v_id, best_topic, second_best_topic):
    d2v_identifier = get_d2v_identifier(d2v_id)
    space_separated_words = space_separated_words.lower()
    if not hpv_version:
        return no_hpv(d2v_identifier, space_separated_words)
    elif hpv_version == 1:
        return hpv_with_par_sent_subsent(d2v_identifier, space_separated_words)
    elif hpv_version == 2:
        return hpv_with_par_sent(d2v_identifier, space_separated_words)
    elif hpv_version == 3:
        return hpv_with_par_sent_subsentnv(d2v_identifier, space_separated_words)
    elif hpv_version == 4:
        return hpv_with_topics(d2v_identifier, space_separated_words, best_topic, second_best_topic)
    elif hpv_version == 5:
        return hpv_with_par_sent_and_topics(d2v_identifier, space_separated_words, best_topic, second_best_topic)
    elif hpv_version == 6:
        return hpv_with_par(d2v_identifier, space_separated_words)
    elif hpv_version == 7:
        return hpv_with_par_and_topics(d2v_identifier, space_separated_words, best_topic, second_best_topic)


def no_hpv(d2v_identifier, space_separated_words):
    space_separated_words = space_separated_words.replace(' paragraphend', '')
    space_separated_words = space_separated_words.replace(' sentenceend', '')
    space_separated_words = space_separated_words.replace(' subsentenceend', '')
    return [create_tagged_document([d2v_identifier], space_separated_words.split(' '))]


def hpv_with_topics(d2v_identifier, space_separated_words, best_topic, second_best_topic):
    space_separated_words = space_separated_words.replace(' paragraphend', '')
    space_separated_words = space_separated_words.replace(' sentenceend', '')
    space_separated_words = space_separated_words.replace(' subsentenceend', '')
    tags = [d2v_identifier, best_topic_label(best_topic), second_best_topic_label(second_best_topic)]
    return [create_tagged_document(tags, space_separated_words.split(' '))]


def hpv_with_par_sent_subsent(d2v_identifier, space_separated_words):
    labeled_sentences = []
    for paragraph_index, paragraph_text in enumerate(space_separated_words.split('paragraphend')):
        paragraph_identifier = '{}_PARA{}'.format(d2v_identifier, paragraph_index)
        for sentence_index, sentence_text in enumerate(paragraph_text.split(' sentenceend')):
            sentence_identifier = '{}_SENT{}'.format(paragraph_identifier, sentence_index)
            for sub_sentence_index, sub_sentence_text in enumerate(sentence_text.split(' subsentenceend')):
                sub_sentence_identifier = '{}_SSENT{}'.format(sentence_identifier, sub_sentence_index)

                words = [s for s in sub_sentence_text.split(' ') if len(s.strip(' ')) > 0]
                tags = [d2v_identifier, paragraph_identifier, sentence_identifier, sub_sentence_identifier]
                labeled_sentences.append(create_tagged_document(tags, words))
    return labeled_sentences


def hpv_with_par_sent(d2v_identifier, space_separated_words):
    labeled_sentences = []
    for paragraph_index, paragraph_text in enumerate(space_separated_words.split('paragraphend')):
        paragraph_identifier = '{}_PARA{}'.format(d2v_identifier, paragraph_index)
        for sentence_index, sentence_text in enumerate(paragraph_text.split(' sentenceend')):
            sentence_identifier = '{}_SENT{}'.format(paragraph_identifier, sentence_index)
            sentence_text = sentence_text.replace(' subsentenceend', '')

            words = [s for s in sentence_text.split(' ') if len(s.strip(' ')) > 0]
            tags = [d2v_identifier, paragraph_identifier, sentence_identifier]
            labeled_sentences.append(create_tagged_document(tags, words))
    return labeled_sentences


def hpv_with_par_sent_subsentnv(d2v_identifier, space_separated_words):
    labeled_sentences = []
    for paragraph_index, paragraph_text in enumerate(space_separated_words.split('paragraphend')):
        paragraph_identifier = '{}_PARA{}'.format(d2v_identifier, paragraph_index)
        for sentence_index, sentence_text in enumerate(paragraph_text.split(' sentenceend')):
            sentence_identifier = '{}_SENT{}'.format(paragraph_identifier, sentence_index)
            for sub_sentence_index, sub_sentence_text in enumerate(sentence_text.split(' subsentenceend')):
                words = [s for s in sub_sentence_text.split(' ') if len(s.strip(' ')) > 0]
                tags = [d2v_identifier, paragraph_identifier, sentence_identifier]
                labeled_sentences.append(create_tagged_document(tags, words))
    return labeled_sentences


# version 6
def hpv_with_par(d2v_identifier, space_separated_words):
    labeled_sentences = []
    for paragraph_index, paragraph_text in enumerate(space_separated_words.split('paragraphend')):
        paragraph_identifier = '{}_PARA{}'.format(d2v_identifier, paragraph_index)
        paragraph_text = paragraph_text.replace(' subsentenceend', '')
        paragraph_text = paragraph_text.replace(' sentenceend', '')

        words = [s for s in paragraph_text.split(' ') if len(s.strip(' ')) > 0]
        tags = [d2v_identifier, paragraph_identifier]
        labeled_sentences.append(create_tagged_document(tags, words))
    return labeled_sentences


def hpv_with_par_sent_and_topics(d2v_identifier, space_separated_words, best_topic, second_best_topic):
    labeled_sentences = []
    for paragraph_index, paragraph_text in enumerate(space_separated_words.split('paragraphend')):
        paragraph_identifier = '{}_PARA{}'.format(d2v_identifier, paragraph_index)
        for sentence_index, sentence_text in enumerate(paragraph_text.split(' sentenceend')):
            sentence_identifier = '{}_SENT{}'.format(paragraph_identifier, sentence_index)
            sentence_text = sentence_text.replace(' subsentenceend', '')
            words = [s for s in sentence_text.split(' ') if len(s.strip(' ')) > 0]
            tags = [d2v_identifier, paragraph_identifier, sentence_identifier, best_topic_label(best_topic),
                    second_best_topic_label(second_best_topic)]
            labeled_sentences.append(create_tagged_document(tags, words))
    return labeled_sentences


# version 7
def hpv_with_par_and_topics(d2v_identifier, space_separated_words, best_topic, second_best_topic):
    labeled_sentences = []
    for paragraph_index, paragraph_text in enumerate(space_separated_words.split('paragraphend')):
        paragraph_identifier = '{}_PARA{}'.format(d2v_identifier, paragraph_index)
        paragraph_text = paragraph_text.replace(' subsentenceend', '')
        paragraph_text = paragraph_text.replace(' sentenceend', '')

        words = [s for s in paragraph_text.split(' ') if len(s.strip(' ')) > 0]
        tags = [d2v_identifier, paragraph_identifier, best_topic_label(best_topic), second_best_topic_label(second_best_topic)]
        labeled_sentences.append(create_tagged_document(tags, words))
    return labeled_sentences


def best_topic_label(best_topic):
    return 'besttopic{}'.format(best_topic)


def second_best_topic_label(second_best_topic):
    return 'secondtopic{}'.format(second_best_topic)
