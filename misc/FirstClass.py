from LoggingModule import _logger as log


class First:

    def hello(self):
        log.info('From inside..')


def mod_hello():
    log.info('from Module Hello')
