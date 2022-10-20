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
    programDir = os.path.abspath('.')
    testFolder = os.path.join(programDir, 'test')
    filesAtDir = glob.glob(os.path.join(testFolder, '*'))
    fileWithExtensions = []
    uniqueExtensions = []
    for path in filesAtDir:
        root, ext = os.path.splitext(path)
        head, filename = os.path.split(path)
        if ext not in uniqueExtensions:
            uniqueExtensions.append(ext)
        fileWithExtensions.append({'path': path, 'name': filename, 'ext': ext})
    logger.info(uniqueExtensions)
    for extension in uniqueExtensions:
        newDirName = os.path.join(programDir, f'Test_{extension[1:]}')
        os.mkdir(newDirName)
    logger.info('New folder created')
    for file in fileWithExtensions:
        newDirName = os.path.join(programDir, f'Test_{file["ext"][1:]}')
        newFileName = os.path.join(newDirName, file["name"])
        os.chmod(file['path'], stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        os.replace(file['path'], newFileName)
    logger.info('Files moved')


if __name__ == '__main__':
    task4()
