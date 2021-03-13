'''
'''
import os
import sys
import platform
import logging


LOG_LEVELS = {
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG}


def set_logger(dir_logging='logs-test',
               filename_datepart='19000101',
               loglevels='debug,info,error,critical'):

    if not os.path.isdir(dir_logging):
        command = f'mkdir {dir_logging}'
        os.system(command)

    requested_log_levels = (loglevels).upper().split(',')

    LOG_FORMAT_FILE = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
    LOG_FORMAT_CONSOLE = '%(name)-12s: %(levelname)-8s %(message)s'

    log_formatter_file = logging.Formatter(LOG_FORMAT_FILE, datefmt='%H:%M:%S')
    log_formatter_console = logging.Formatter(LOG_FORMAT_CONSOLE)

    # comment this to suppress console output
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter_console)
    logging.getLogger('').addHandler(stream_handler)
    logging.getLogger('').setLevel(logging.DEBUG)

    for requested_level in requested_log_levels:
        if (requested_level == 'DEBUG') and (platform.system() != 'Darwin'):
            continue
        if requested_level in LOG_LEVELS.keys():
            log_file = f'{dir_logging}/{filename_datepart}.{requested_level}.log'
            file_handler = logging.FileHandler(
                log_file, mode='a', encoding='utf-8')
            file_handler.setFormatter(log_formatter_file)
            file_handler.setLevel(LOG_LEVELS[requested_level])
            logging.getLogger('').addHandler(file_handler)

    logger = logging.getLogger('libLogger')

    logger.debug('--------- liblogger initiated ---------')


def test_logger():
    set_logger()


if __name__ == '__main__':
    test_logger()
