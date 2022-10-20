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


def getFilesList(directory):
    files = []
    for file in os.listdir(directory):
        size = os.path.getsize(os.path.join(directory, file))
        files.append((file, size))
    return files


def task2():
    programDir = os.path.abspath('.')
    testDir = os.path.join(programDir, 'Test')
    dir1Path = os.path.join(testDir, 'folder1')
    dir2Path = os.path.join(testDir, 'folder2')
    files1 = getFilesList(dir1Path)
    files2 = getFilesList(dir2Path)
    intersection = [value for value in files1 if value in files2]
    logger.info('Same files in folder1 and f'
                'older2:')
    for file in intersection:
        logger.info(f'{file[0]} \t with {file[1]} bytes')


if __name__ == '__main__':
    task2()
