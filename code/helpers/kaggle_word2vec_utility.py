import subprocess
import gensim


class KaggleWord2VecUtility(object):
    # @staticmethod
    # def convert_review(text):
    # cmd = "LC_ALL=C awk '{print tolower($0);}' | sed -e 's/\./ \. /g' -e 's/<br \/>/ /g' -e 's/\"/ \" /g'" \
    #       " -e 's/,/ , /g' -e 's/(/ ( /g' -e 's/)/ ) /g' -e 's/\!/ \! /g' -e 's/\?/ \? /g' " \
    #       " -e 's/\;/ \; /g' -e 's/\:/ \: /g'"
    # ret = subprocess.check_output(cmd, shell=True, input=gensim.utils.to_utf8(text))
    # return ret.strip()

    @staticmethod
    def review_to_word_list(review):
        # if True:
        #    review = KaggleWord2VecUtility.convert_review(review)
        # stops = set(stopwords.words("english"))
        # words = [w for w in words if w not in stops]
        return gensim.utils.to_unicode(review.lower()).split()
