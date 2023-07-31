import logging


class GlobalLogger:
    _initialized = False

    @classmethod
    def initialize(cls, log_level=logging.INFO, log_file=None):
        if not cls._initialized:
            logger = logging.getLogger()
            logger.setLevel(log_level)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

            if log_file:
                file_handler = logging.FileHandler(log_file)
                file_handler.setLevel(log_level)
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)

            cls._initialized = True


GlobalLogger.initialize(log_level=logging.DEBUG)