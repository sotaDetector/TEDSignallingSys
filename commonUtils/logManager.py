import logging


class logUtils:
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    @staticmethod
    def info(data):
        logging.info(data)