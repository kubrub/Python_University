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


def task2():
    programDirectory = os.path.abspath('.')
    logger.info(f"Program folder: {programDirectory}")
    testDirectory = os.path.join(programDirectory, "test")
    logger.info(f"Test folder: {programDirectory}")
    filesAtDirectory = glob.glob(os.path.join(testDirectory, '*.txt'))
    logger.info(f"Get .txt files")
    notepadPath = "C:\\Program Files\\Notepad++\\notepad++.exe"
    params = filesAtDirectory.copy()
    params.insert(0, " ")
    logger.info(f"Start run files:{filesAtDirectory}")
    os.execvp(notepadPath, params)


if __name__ == '__main__':
    task2()
