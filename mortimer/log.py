import logging
import sys

from config import Config

log_level = Config.llevel
logging.basicConfig(level=log_level)
logger = logging.getLogger(Config.app_name)
logger.propagate = False

INFO_FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s'
DEBUG_FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s ' \
               '[in %(pathname)s:%(lineno)d]'
TIMESTAMP_FORMAT = '%d-%m-%Y %H:%M:%S %z'

ALEMBIC_LOG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(levelname)-8s] %(asctime)-15s,%(msecs)03d (%(name)s): %(message)s',
            'datefmt': '%Y-%m-%d %I:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        },
    },
    'root': {
        'level': log_level,
        'handlers': ['console'],
    },
}

if log_level == 'INFO':
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(
        logging.Formatter(INFO_FORMAT, TIMESTAMP_FORMAT))
    logger.addHandler(stream_handler)

if log_level == 'DEBUG':
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(
        logging.Formatter(DEBUG_FORMAT, TIMESTAMP_FORMAT))
    logger.addHandler(stream_handler)


def get_logger():
    return logger