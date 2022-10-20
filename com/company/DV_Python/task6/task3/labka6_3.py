import os
import os.path
import glob
import stat

def task3():
    extension = input('Please enter extension (txt, pdf, etc.):')
    programDir = os.path.abspath('.')
    testDir = os.path.join(programDir, 'Test')
    dirs = os.listdir(testDir)
    anyFiles = False
    print(f'\nFiles with {extension} extension:')
    for d in dirs:
        path = os.path.join(testDir, d)
        files = os.listdir(path)
        for file in files:
            root, ext = os.path.splitext(file)
            if  extension in ext:
                print(f'{file} - in {d}')
                anyFiles = True
    if(not(anyFiles)):
        print("There are not files with {extension} in these directories")

if __name__ == '__main__':
    task3()
