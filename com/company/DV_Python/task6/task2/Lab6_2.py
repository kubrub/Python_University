import os
import os.path
import glob
import time
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


def getListOfFilesInDirectory(directory):
    files = []
    for file in os.listdir(directory):
        size = os.path.getsize(os.path.join(directory, file))
        files.append((file, size))  
    return files


def task2():
    programFolder = os.path.abspath('.')
    testFolder = os.path.join(programFolder, 'Test')
    folder1Path = os.path.join(testFolder, 'Folder1')
    folder2Path = os.path.join(testFolder, 'Folder2')
    filesFromFolder1 = getListOfFilesInDirectory(folder1Path)
    filesFromFolder2 = getListOfFilesInDirectory(folder2Path)
    intersection = [value for value in filesFromFolder1 if value in filesFromFolder2]
    logger.info('Same files in Folder1 and Folder2:')
    for file in intersection:
        logger.info(f'{file[0]} \t with {file[1]} bytes')


if __name__ == '__main__':
    task2()
