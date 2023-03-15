import bmp_to_bmp
import tiff_method
import jpeg_file


def menu():
    print("1 - зберегти зображення у форматі ВМР (стиснення за методом RLE)")
    print("2 - зберегти зображення у  форматі TIFF (стиснення за методом LZW)")
    print("3 - зберегти зображення у  форматі форматі JPEG (використовувати стандартне кодування Standard Encoding)")
    print("0 - вийти з програми")


def main():
    name_of_photo = ""
    print("Привіт - це консольна програма")
    menu()
    command = input_command()
    while command != 0:
        if command == 1:
            print("\n1 command\n")
            bmp_to_bmp.bmp(name_of_photo)
        elif command == 2:
            print("\n2 command\n")
            tiff_method.convert_to_tiff(name_of_photo)
        elif command == 3:
            print("\n3 command\n")
            jpeg_file.
        elif command == 0:
            exit()
        else:
            print("\nInvalid command, try again\n")
        menu()
        command = input_command()


def input_command():
    return int(input("Будь ласка введіть номер команди:\n"))


if __name__ == '__main__':
    main()

