import os
import os.path
import glob
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


def task1():
    programDirectory = os.path.abspath('.')
    logger.info(f"Program folder: {programDirectory}")
    testDirectory = os.path.join(programDirectory, 'test')
    logger.info(f"Test folder: {testDirectory}")
    bmpFile = glob.glob(os.path.join(testDirectory, '*.bmp'))[0]
    logger.info(f"Get .bmp file path {bmpFile}")
    wordFile = glob.glob(os.path.join(testDirectory, '*.docx'))[0]
    logger.info(f"Get .docx file path {wordFile}")
    os.startfile(bmpFile)
    logger.info(f"Start .bmp file")
    os.startfile(wordFile)
    logger.info(f"Start .docx file")


if __name__ == '__main__':
    task1()
