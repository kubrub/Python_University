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
    programDir = os.path.abspath('.')
    logger.info(f"Program folder: {programDir}")
    testDir = os.path.join(programDir, 'Test')
    logger.info(f"Test folder: {testDir}")
    bmpFile = glob.glob(os.path.join(testDir, '*.bmp'))[0]
    logger.info(f"Get .bmp file path {bmpFile}")
    wordFile = glob.glob(os.path.join(testDir, '*.docx'))[0]
    logger.info(f"Get .docx file path {wordFile}")
    os.system(bmpFile)
    logger.info(f"Start .bmp file")
    os.system(wordFile)
    logger.info(f"Start .docx file")


if __name__ == '__main__':
    task1()
