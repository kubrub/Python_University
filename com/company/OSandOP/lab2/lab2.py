import os, glob
from datetime import datetime


def log(logTxt):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  # get today's day
    with open("information_for_lab_2.txt", 'a') as f:
        f.write('[{}]:{}\n'.format(dt_string, logTxt))  # write log to file


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')  # format data to "day mounth year"
    return formated_date


def find_files():
    files = glob.glob(r'./**/*.dat', recursive=True)  # find all .dat files in current directory or in sub directories
    log("Found {} files:".format(len(files)) + "".join(" " + x for x in files))
    return files


def get_names(files):
    names = []
    for x in files:
        names.append(os.path.split(x)[-1])  # get names of files
    log("Got file names")
    return names


def get_fullpath(path):
    full_path = os.path.abspath(path)  # get full path to the file
    log("Got full path to file - " + full_path)
    return full_path


def get_filecontent(path):
    text = str()
    with open(path, 'r') as f:
        text = f.read()  # read all data from file
    log("Got content of file - " + path)
    return text


def get_fileinfo(path):
    file_data = {'size': os.path.getsize(path),  # get file size in bytes
                 'creation_time': convert_date(os.path.getctime(path))}  # get creation time of the file
    log("Got info about file - " + path)
    return file_data


def calc(path, exception_digit=0):
    sm = 0
    log("The calculation of the sum has started in the file " + path)
    for x in get_filecontent(path).split():  # calculate sum of numbers in file
        try:
            sm += int(x)
        except:
            log("Сorrupted data {} was found and replaced with {}".format(x, exception_digit))
            sm += exception_digit  # replace corrupted naumber with exception_digit
    log("Sum has been calculated")
    return sm


def main():
    log("Program has started")
    files = find_files()  # find all .dat files
    subst_num = 0
    print('Choose file: ')
    i = 1
    for x in get_names(files):
        print("{} - {}".format(i, x))
        i += 1
    print('{} - settings'.format(i))
    inp = int(input())  # select option
    while inp == i:  # open setting dialog
        subs_num = int(input("Chose number to replace corrupted data: "))  # set new number for substitution
        log('Replacing number was changed to {}'.format(subs_num))
        inp = int(input("Chose file: "))  # select option
        try:
            chosen_file = files[inp - 1]  # select file
        except:
            chosen_file = files[-1]  # select last file in case of exception
    else:
        try:
            chosen_file = files[inp - 1]  # select file
        except:
            chosen_file = files[-1]  # select last file in case of exception
    log('File {} chosen'.format(chosen_file))
    print("Full path to file: \n\t{}".format(get_fullpath(chosen_file)))  # show full path to the file
    file_inf = get_fileinfo(chosen_file)
    print("File creation time: {}\nFile size: {} bytes".format(file_inf['creation_time'],
                                                               file_inf['size']))  # show info about the file
    print("File content:\n\t{}".format(get_filecontent(chosen_file)))  # show file content
    print("The sum of numbers in the file: {}".format(calc(chosen_file, subst_num)))  # show sum of numbers in file
    input("Press any button to finish")
    log("Program has finished")


if __name__ == "__main__": main()

