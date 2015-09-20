import re
import subprocess
import gensim

from helpers.log_config import get_log_output


def say_result(log_handler, log_buffer):
    output = get_log_output(log_handler, log_buffer)
    score = float(re.findall('Score: (\d+\.?\d*)%', output)[0])
    subprocess.call(['say', 'New score: {:.2f}%!'.format(score)])
