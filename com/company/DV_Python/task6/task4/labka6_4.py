import os
import os.path
import glob
import stat
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


def task4():
    programDirectory = os.path.abspath('.')
    testDirectory = os.path.join(programDirectory, 'test')
    filesAtDirectory = glob.glob(os.path.join(testDirectory, '*'))
    fileWithExtensions = []
    uniqueExtensions = []
    for path in filesAtDirectory:
        root, extensions = os.path.splitext(path)
        head, filename = os.path.split(path)
        if extensions not in uniqueExtensions:
            uniqueExtensions.append(extensions)
        fileWithExtensions.append({'path': path, 'name': filename, 'ext': extensions})
    logger.info(uniqueExtensions)
    for extension in uniqueExtensions:
        newDirName = os.path.join(programDirectory, f'test_{extension[1:]}')
        os.mkdir(newDirName)
    logger.info('new folder created')
    for file in fileWithExtensions:
        newDirName = os.path.join(programDirectory, f'test_{file["ext"][1:]}')
        newFileName = os.path.join(newDirName, file["name"])
        os.chmod(file['path'], stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        os.replace(file['path'], newFileName)
    logger.info('files moved')


if __name__ == '__main__':
    task4()
