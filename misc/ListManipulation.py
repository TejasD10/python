import logging
def main():
    # Create a list
    logger = logging.getLogger(__name__)
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    logger.info('List entered: ' + str(a))


    count = 0
    return sum(1 for _ in a)


if __name__ == '__main__':
    print(main())
