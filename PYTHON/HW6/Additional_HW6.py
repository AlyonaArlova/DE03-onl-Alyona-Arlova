import users
import stats
import shop
import text_analyzer
import numbers

#1. Напишите программу в модуле main.py, которая запрашивает у пользователя имя и возраст,
# используя функцию register_user() из модуля users.py. Если возраст меньше 18,
# программа должна вывести «Доступ ограничен», иначе — «Добро пожаловать, {имя}!».
# Результат работы функции (имя и возраст) не обязательно сохранять в файл,
# но можно вернуть как строку и вывести на экран.

name = input("Please enter your name: ")
age = input("Please enter your age: ")
users.register_user(name, age)

#2. Создайте программу в модуле main.py, которая с помощью функции calculate_stats(numbers) из модуля stats.py
# принимает от пользователя строку чисел, преобразует её в список, находит сумму, максимальное и минимальное значение.
# Если сумма больше 100, выводится сообщение «Большая сумма».
# Работа с файлами в этой задаче не используется, результаты просто выводятся на экран.

input_str = input("Please enter any number separated by space: ")
stats.calculate_stats(input_str)


#3.Реализуйте программу в модуле main.py, которая использует функцию make_order(product, qty)
# из модуля shop.py для оформления заказа. В модуле shop.py хранится словарь с товарами и их ценами.
# Пользователь вводит название товара и количество, функция проверяет, есть ли такой товар,
# и если он найден, считает общую стоимость и возвращает строку с информацией о заказе.
# Если товара нет — возвращается сообщение «Товар не найден». Заказы сохраняются в файл orders.txt.

while True:
    product = input("Enter product name (or 'q' to quit): ")
    if product.lower() == 'q':
        print("Exit")
        break

    qty_input = input("Enter product quantity (or 'q' to quit): ")
    if qty_input.lower() == 'q':
        print("Exit")
        break

    try:
        qty = int(qty_input)
        if qty <= 0:
            print("Quantity must be > 0")
            continue
    except ValueError:
        print("Please enter a valid number for quantity")
        continue

    shop.make_order(product, qty)



#4.Напишите программу в модуле main.py, которая вызывает функцию filter_even_numbers(input_file, output_file) из модуля numbers.py.
# Входной файл содержит числа по одному в строке. Функция должна считать все числа,
# отфильтровать только чётные и сохранить их в другой файл, а также вернуть количество найденных чётных чисел,
# которое выводится в консоль.
input_file = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/HW6/input_file.txt"
output_file = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/HW6/output_file.txt"
numbers.filter_even_numbers(input_file, output_file)

#5.Создайте программу в модуле main.py, которая использует функцию analyze_file(path) из модуля text_analyzer.py.
# Функция считывает содержимое указанного текстового файла, определяет количество строк,
# количество слов и самое длинное слово, а затем возвращает эти данные в виде строки.
# Программа выводит результат в консоль и сохраняет его в файл analysis.txt.
path = input("Please enter file path")
result = text_analyzer.analyze_file(path)
print(result)

with open("/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/HW6/analysis.txt", "w") as f:
    f.write(result)

if "Файл не найден" not in result and "Произошла ошибка" not in result:
    with open("/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/HW6/analysis.txt", "w") as f:
        f.write(result)
