import os
import os.path
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


def task3():
    extension = input('Please enter extension (txt, pdf, etc.):')
    programDirectory = os.path.abspath('.')
    testDirectory = os.path.join(programDirectory, 'test')
    dirs = os.listdir(testDirectory)
    filesInFolder = False
    logger.info(f'Files with {extension} extension:')
    for d in dirs:
        path = os.path.join(testDirectory, d)
        files = os.listdir(path)
        for file in files:
            root, ext = os.path.splitext(file)
            if extension in ext:
                logger.info(f'{file} - in {d}')
                filesInFolder = True
    if not filesInFolder:
        logger.info("There are not files with {extension} in these directories")


if __name__ == '__main__':
    task3()
