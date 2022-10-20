import os
import os.path
import glob
import stat


def task4():
    programDir = os.path.abspath('.')
    testFolder = os.path.join(programDir, 'Test')
    filesAtDir = glob.glob(os.path.join(testFolder, '*'))
    fileWithExtensions = []
    uniqueExtensions = []
    for path in filesAtDir:
        root, ext = os.path.splitext(path)
        head, filename = os.path.split(path)
        if ext not in uniqueExtensions:
            uniqueExtensions.append(ext)
        fileWithExtensions.append({'path': path, 'name': filename, 'ext':ext})
    print(uniqueExtensions)
    for extension in uniqueExtensions:
        newDirName = os.path.join(programDir, f'Test_{extension[1:]}')
        os.mkdir(newDirName)
    print('New folder created')
    for file in fileWithExtensions:
        newDirName = os.path.join(programDir, f'Test_{file["ext"][1:]}')
        newFileName = os.path.join(newDirName, file["name"])
        os.chmod(file['path'], stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO)
        os.replace(file['path'], newFileName)
    print('Files moved')


if __name__ == '__main__':
    task4()
