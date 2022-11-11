import json
import os
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


def printAllQuestionsByCategory(data, category):
    logger.info("~~~Print all questions by category name~~~")
    categoryRecord = data[category]
    logger.info(f'~~~Print all questions at {category}~~~')
    for key in categoryRecord.keys():
        question = categoryRecord[key]
        for questionKey in question.keys():
            logger.info(f"\t{questionKey}: {question[questionKey]}")


def findValuesByKey(data, key):
    logger.info("~~~~~Find all values by key~~~~~")
    logger.info(f'~~~Find all values by key: {key}~~~')
    findValuesByKeyHelper(data, key)


def findValuesByKeyHelper(data, key):
    logger.info("~~~~~Find all values by key recursive helper~~~~~")
    key1 = data.keys()
    for k in key1:
        if k == key:
            logger.info(f'\t{data[k]}')
        elif isinstance(data[k], dict):
            findValuesByKeyHelper(data[k], key)


def findByKeyValuePair(data, key, value):
    logger.info("~~~~~Find object by key value~~~~~")
    logger.info(f'\nPrint {key} with value {value}')
    findByKeyValuePairHelper(data, key, value)


def findByKeyValuePairHelper(data, key, value):
    logger.info("~~~~~Find object by key value recursive helper~~~~~")
    key1 = data.keys()
    for k in key1:
        if k == key:
            if data[k] == value:
                logger.info(data)
        elif isinstance(data[k], dict):
            findByKeyValuePairHelper(data[k], key, value)


def task4(filename):
    logger.info('~~~~~Reading file~~~~~')
    with open(filename) as data_file:
        data = json.load(data_file)
    quiz = data['quiz']

    printAllQuestionsByCategory(quiz, 'maths')
    findValuesByKey(quiz, 'question')
    findByKeyValuePair(data, 'question', '5 + 7 = ?')


def main():
    filename = os.path.join(os.path.abspath("."), "quiz.json")
    task4(filename)


if __name__ == "__main__":
    main()
