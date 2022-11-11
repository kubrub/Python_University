import urllib.request
import os
import json
import logging
import sys


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


def task1(filename):
    logger.info('~~~~~~~~~Loading~~~~~~~~~')
    url = 'https://support.oneskyapp.com/hc/en-us/article_attachments/202761727/example_2.json'
    remoteFile = urllib.request.urlopen(url)

    logger.info('~~~~~~~~~Get file from server~~~~~~~~~')
    with open(filename, 'wb') as file:
        file.write(remoteFile.read())
        logger.info('~~~~~~~~~File was saved~~~~~~~~~')

    remoteFile.close()
    logger.info('~~~~~~~~~File closed~~~~~~~~~')


def task2(filename):
    logger.info('~~~~~~~~~Print file to console: ~~~~~~~~~')
    with open(filename) as data_file:
        data = json.load(data_file)
    logger.info(data)

    logger.info('~~~~~~~~~Printing finished~~~~~~~~~')
    logger.info('~~~~~~~~~Opening file~~~~~~~~~')
    os.startfile(filename)


def main():
    filename = os.path.join(os.path.abspath("."), "quiz.json")
    task1(filename)
    task2(filename)


if __name__ == "__main__":
    main()
