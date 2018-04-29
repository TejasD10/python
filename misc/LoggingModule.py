from logging.handlers import RotatingFileHandler

import FirstClass
import ListManipulation

_logger = logging.getLogger(__name__)
_logFile = RotatingFileHandler('C:/Users/TDesai/Desktop/PythonLog.log', maxBytes=209715200, backupCount=2)
_logger.setLevel(logging.DEBUG)
_logFile.setFormatter(logging.Formatter('%(module)-18s [%(asctime)-3s] - %(levelname)-5s - %(message)s'))
_logger.addHandler(_logFile)


def main():
    _logger.info('Main Executed')
    ListManipulation.main()
    first = FirstClass.First()
    first.hello()
    FirstClass.mod_hello()


if __name__ == '__main__':
    main()
