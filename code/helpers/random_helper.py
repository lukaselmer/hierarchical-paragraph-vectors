from datetime import datetime
import random

import numpy


def init_random():
    random.seed(datetime.now())
    numpy.random.seed(random.randint(0, 4294967295))
    return random.random()


def random_int():
    return random.randint(0, 4294967295)
