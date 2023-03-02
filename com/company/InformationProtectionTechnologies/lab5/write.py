import easygui


def writeToFile(data):
    filename1 = easygui.fileopenbox()

    with open(filename1, "w") as data_file:
        data_file.write(data)


data = 'something'
writeToFile(data)