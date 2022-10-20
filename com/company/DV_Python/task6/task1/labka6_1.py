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


def printFileNameAndTheirTime(name, time):
    logger.info(f'{name} - {time.tm_mday}/{time.tm_mon}/{time.tm_year} {time.tm_hour}:{time.tm_min}:{time.tm_sec}')


def task1():
    programDirectory = os.path.abspath('.')
    testDirectory = os.path.join(programDirectory, 'Test')
    filesInDirectory = glob.glob(os.path.join(testDirectory, '*'))
    fileNamesAndTheirCreatingTime = []
    logger.info('List of all files with creation time:')
    for path in filesInDirectory:
        head, fileName = os.path.split(path)
        globalCreatedTime = os.path.getmtime(path)
        localCreatedTime = time.localtime(globalCreatedTime)
        printFileNameAndTheirTime(fileName, localCreatedTime)
        fileNamesAndTheirCreatingTime.append({'name': fileName, 'time': localCreatedTime})

    fileNamesAndTheirCreatingTime.sort(key=lambda x: x['time'])
    fileNamesWithTimeLength = len(fileNamesAndTheirCreatingTime)
    if fileNamesWithTimeLength == 2:
        logger.info('Two oldest files and two latest files are the same:')
        printFileNameAndTheirTime(fileNamesAndTheirCreatingTime[0]['name'], fileNamesAndTheirCreatingTime[0]['time'])
        printFileNameAndTheirTime(fileNamesAndTheirCreatingTime[1]['name'], fileNamesAndTheirCreatingTime[1]['time'])
    elif fileNamesWithTimeLength > 2:
        logger.info('Two oldest files:')
        printFileNameAndTheirTime(fileNamesAndTheirCreatingTime[0]['name'], fileNamesAndTheirCreatingTime[0]['time'])
        printFileNameAndTheirTime(fileNamesAndTheirCreatingTime[1]['name'], fileNamesAndTheirCreatingTime[1]['time'])

        logger.info('Two latest files:')
        printFileNameAndTheirTime(fileNamesAndTheirCreatingTime[fileNamesWithTimeLength - 1]['name'],
                                  fileNamesAndTheirCreatingTime[fileNamesWithTimeLength - 1]['time'])
        printFileNameAndTheirTime(fileNamesAndTheirCreatingTime[fileNamesWithTimeLength - 2]['name'],
                                  fileNamesAndTheirCreatingTime[fileNamesWithTimeLength - 2]['time'])


if __name__ == '__main__':
    task1()

