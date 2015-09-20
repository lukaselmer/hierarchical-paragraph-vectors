try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import logging

import pandas


def log_to_info(output):
    logging.info(output)


def setup_logger(log_to_buffer=False):
    pandas.set_option('display.width', 1000)

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    if log_to_buffer:
        log_buffer = StringIO()
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)

        log_handler = logging.StreamHandler(log_buffer)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_handler.setFormatter(formatter)
        root_logger.addHandler(log_handler)

        return log_handler, log_buffer


def get_log_output(log_handler, log_buffer):
    log_handler.flush()
    log_buffer.flush()
    output = log_buffer.getvalue()
    return output
