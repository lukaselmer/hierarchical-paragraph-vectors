import logging

from algorithms.Word2Vec_ParagraphVectors import main
from helpers.api import get_random_pending_run, report_results
from helpers.log_config import setup_logger, log_to_info, get_log_output


def slave_main():
    log_handler, log_buffer = setup_logger(True)
    run = get_random_pending_run()
    # noinspection PyBroadException
    try:
        if not run:
            log_to_info('Nothing to start, exiting')
            return
        # log_to_info('NothingScore: 77.7% to start, exiting')
        main(run=run)
    except Exception:
        logging.exception('Unknown error')

    output = get_log_output(log_handler, log_buffer)
    report_results(run['id'], output)


if __name__ == '__main__':
    slave_main()
