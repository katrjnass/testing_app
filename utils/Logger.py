import logging


class Logger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - '
                                          '%(funcName)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', style='%')
        self.create_handler(logging.FileHandler('tests.log', mode='w'), formatter)
        self.create_handler(logging.StreamHandler(), formatter)

    def get_logger(self):
        return self.logger

    @staticmethod
    def create_handler(handler, formatter, level=logging.INFO):
        handler.setFormatter(formatter)
        handler.setLevel(level)
        logging.getLogger(__name__).addHandler(handler)
