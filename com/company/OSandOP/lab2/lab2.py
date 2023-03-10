import os
import glob
from datetime import datetime


# отримуємо сьогоднішній день та записуємо у файл
def get_day_and_write_to_log_file(logTxt):
    today = datetime.now()
    dt_string = today.strftime("%d/%m/%Y %H:%M:%S")
    with open("information_for_lab_2.txt", 'a') as f:
        f.write('[{}]:{}\n'.format(dt_string, logTxt))


# форматуємо дані в "день місяць рік"
def convert_date(timestamp):
    day = datetime.utcfromtimestamp(timestamp)
    formated_date = day.strftime('%d %b %Y')
    return formated_date


# знаходимо всі файли .dat у поточному каталозі чи підкаталогах
def find_files_with_dat():
    files = glob.glob(r'./**/*.dat', recursive=True)
    get_day_and_write_to_log_file("Found {} files:".format(len(files)) + "".join(" " + x for x in files))
    return files


# отримуємо назви файлів
def get_names_of_files(files):
    names = []
    for x in files:
        names.append(os.path.split(x)[-1])
    get_day_and_write_to_log_file("Get file names")
    return names


# отримуємо повний шлях до файлу
def get_fullpath_of_file(path):
    full_path = os.path.abspath(path)
    get_day_and_write_to_log_file("Get full path to file - " + full_path)
    return full_path


# читаємо всі дані з файлу
def get_filecontent(path):
    text = str()
    with open(path, 'r') as f:
        text = f.read()
    get_day_and_write_to_log_file("Get content of file - " + path)
    return text


# отримуємо розмір файлу в байтах та час створення файлу
def get_fileinfo(path):
    file_data = {'size': os.path.getsize(path),
                 'creation_time': convert_date(os.path.getctime(path))}
    get_day_and_write_to_log_file("Got info about file - " + path)
    return file_data


# обчислюємо суму чисел у файлі
def calculation(path, exception_digit=0):
    sm = 0
    get_day_and_write_to_log_file("The calculation of the sum has started in the file " + path)
    for x in get_filecontent(path).split():
        try:
            sm += int(x)
        except:
            get_day_and_write_to_log_file("Corrupted data {} was found and replaced with {}".format(x, exception_digit))
            sm += exception_digit
    get_day_and_write_to_log_file("Sum has been calculated")
    return sm


def main():
    get_day_and_write_to_log_file("Program has started")
    files = find_files_with_dat()
    subst_num = 0
    print('Choose file: ')
    i = 1
    for x in get_names_of_files(files):
        print("{} - {}".format(i, x))
        i += 1
    print('{} - settings'.format(i))
    inp = int(input())
    while inp == i:
        subs_num = int(input("Chose number to replace corrupted data: "))
        get_day_and_write_to_log_file('Replacing number was changed to {}'.format(subs_num))
        inp = int(input("Chose file: "))
        try:
            chosen_file = files[inp - 1]
        except:
            chosen_file = files[-1]
    else:
        try:
            chosen_file = files[inp - 1]
        except:
            chosen_file = files[-1]
    get_day_and_write_to_log_file('File {} chosen'.format(chosen_file))
    print("Full path to file: \n\t{}".format(get_fullpath_of_file(chosen_file)))
    file_inf = get_fileinfo(chosen_file)
    print("File creation time: {}\nFile size: {} bytes".format(file_inf['creation_time'],
                                                               file_inf['size']))
    print("File content:\n\t{}".format(get_filecontent(chosen_file)))
    print(
        "The sum of numbers in the file: {}".format(calculation(chosen_file, subst_num)))  # show sum of numbers in file
    input("Press any button to finish")
    get_day_and_write_to_log_file("Program has finished")


if __name__ == "__main__":
    main()
