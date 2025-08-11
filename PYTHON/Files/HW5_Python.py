#Откройте файл example.txt и выведите его содержимое на экран
file_path = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/Files/example.txt"
with open(file_path, "r") as file:
    content = file.read()
    print(content)

#Создайте файл output.txt и запишите в него строку "Hello, World!"
file_path_task2 = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/Files/output.txt"
with open(file_path_task2, "a+") as file2:
    file2.write("\nHello, World!")
    file2.seek(0)
    print(file2.read())

#Напишите программу,
# которая считает количество строк, слов и символов в заданном текстовом файле и выводит результаты.
file_path_task3 = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/Files/FileForHWTask3.txt"
try:
    with open(file_path_task3,"r+") as file2:
        content = file2.read()
        print("количество символов в заданном текстовом файл:",len(content))
        print("количество слов в заданном текстовом файл:", len(content.split()))
        print("количество строк в заданном текстовом файл:",len(content.splitlines()))

except FileNotFoundError:
    print("File does not exist!")
finally:
    print("Finish!")