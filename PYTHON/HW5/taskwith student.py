#Задание 1: Напишите программу,
# которая считывает содержимое одного файла и записывает его в другой файл.
# Задание 1: считываем содержимое одного файла и записываем его в другой
my_original_file = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/Files/Task1withStudent.txt"
updated_file = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/Files/Task1WriteStudent.txt"

try:
    with open(my_original_file, "r") as MOF, \
         open(updated_file, "w") as UF:
        content = MOF.read()
        UF.write(content.upper())
    with open(updated_file, "r") as UF:
        print(UF.read())

    print("work is done")

except FileNotFoundError:
    print("no such files")
except IsADirectoryError:
    print("Error, check file")

finally:
    print("finish")

