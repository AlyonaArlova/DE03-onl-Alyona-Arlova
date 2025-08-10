# Создайте список fruits с элементами "apple", "banana", "cherry".
# Выведите первый элемент списка.
fruits =["apple", "banana", "cherry"]
print(fruits[0])

#Создайте словарь student с ключами name, age и grade и соответствующими значениями.
#Выведите значение по ключу name.
student_dct = [
    {"name": "Alyona", "age": 18, "marks": 10},
    {"name": "Anna", "age": 17, "marks": 8},
    {"name": "Alex", "age": 18, "marks": 9},
    {"name": "Max", "age": 19, "marks": 7}
]
for student in student_dct:
    print(student["name"])


#Напишите программу, которая создает множество уникальных слов из введенной пользователем строки.
# Программа должна учитывать только уникальные слова и игнорировать регистр.
user_string = input("Enter sentence from keyboard: ")
words = user_string.lower().split()
unique_user_string = set(words)
print("Unique words: ", unique_user_string)

#Напишите программу, которая создает
#список студентов, их возрастов и оценок. Используйте списки, кортежи и словари для хранения данных.
# Программа должна выводить всех студентов, их возраста и оценки, а также производить операции над этими данными.
st_dct = [
    {"name": "Alyona", "age": 18, "marks": 10},
    {"name": "Anna", "age": 17, "marks": 8},
    {"name": "Alex", "age": 18, "marks": 9},
    {"name": "Max", "age": 19, "marks": 7}
]
print("All students:")
for student in st_dct:
    print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")
marks_list = [student["marks"] for student in st_dct] #list of marks
ages_tuple = tuple(student["age"] for student in st_dct) # tuple of ages
average_marks = sum(marks_list) / len(marks_list)
max_marks = max(marks_list)
max_ages = max(ages_tuple)
print(f"Max age: {max_ages}")
print(f"Max mark: {max_marks}")
print(f"Av mark: {average_marks}")


#Создайте два списка: [1, 2, 3] и [4, 5, 6]. Напишите
#программу, которая объединяет эти списки в один и выводит результат.
first_list = [1, 2, 3]
second_list = [4, 5, 6]
both_lists = first_list + second_list
print("Объединенные списки в один", both_lists)
first_list.extend(second_list)
print("Объединненные списки в один", first_list)

#Напишите программу, которая удаляет все
#дубликаты из списка [1, 2, 2, 3, 4, 4, 5] с помощью преобразования в множество и выводит результат
number_list = [1, 2, 2, 3, 1, 4, 4, 5, 5]
unique_number_list = set(number_list)
print("Список без дубликатов",unique_number_list)
