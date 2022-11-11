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


def task3(filename):
    logger.info('~~~~~~~~~Reading file~~~~~~~~~')
    with open(filename) as data_file:
        data = json.load(data_file)

    quiz = data['quiz']
    logger.info('~~~~~~~~~Main info~~~~~~~~~')
    logger.info(f'~~!Amount of quiz category: {len(quiz)}')

    typesOfQuizCategory = [type(quiz[elem]).__name__ for elem in quiz.keys()]
    logger.info(f'~~!Types of quiz category object: {typesOfQuizCategory}:')

    typeOfSportQ1Options = type(quiz['sport']['q1']['options']).__name__
    logger.info(f"~~!Type of 'sport.q1.options': {typeOfSportQ1Options}")

    valueOfSportQ1Options = quiz['sport']['q1']['options']
    logger.info(f"~~!Value of 'sport.q1.options':\n{valueOfSportQ1Options}")

    logger.info("~~!Subjects of 'maths':")
    subvalues = [subvalue for subvalue in quiz['maths'].items()]
    logger.info(subvalues)

    allQuizElements = [str(ob) + ' : ' + str(quiz[ob]) for ob in quiz.keys()]
    logger.info(f'~~!All objects of quiz:')
    logger.info(allQuizElements)


def main():
    filename = os.path.join(os.path.abspath("."), "quiz.json")
    task3(filename)


if __name__ == "__main__":
    main()
