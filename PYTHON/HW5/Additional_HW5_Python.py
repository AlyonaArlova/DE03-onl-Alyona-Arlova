#Напиште программу, которая читает данные из файла students.txt,
# где каждая строка содержит имя и оценку ученика
# (например: Иван 4). Программа должна выбрать только тех учеников, у которых оценка 4 или выше,
# и записать их в новый файл good_students.txt в том же формате.
original_file = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/Files/student.txt"
new_file = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/Files/good_student.txt"
try:
    with open(original_file, "r") as OF, open(new_file, "w") as NF:
        for line in OF:
            content = line.split()
            if int(content[1]) >= 4:
                NF.write(line)
except FileNotFoundError:
    print("Such file does not exist")
finally:
    print("Finish")
