import logging


def configure_logging(log_level):
    """Configures de logger with format and level globally"""
    logging.basicConfig(level=log_level,
                        format='%(asctime)s - %(message)s')
