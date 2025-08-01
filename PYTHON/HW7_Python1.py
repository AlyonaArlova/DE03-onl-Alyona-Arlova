#Напишите программу,которая запрашивает у пользователя строку и
# выводит количество гласных и согласных букв в этой строке.
while True:
    word = input("Введите слово: ").lower()

    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л',
                  'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц',
                  'ч', 'ш', 'щ']
    russian_alphabet = vowels + consonants

    wrong_letter = False
    vowels_count = 0
    consonants_count = 0

    for letter in word:
        if letter in vowels:
            vowels_count += 1
        elif letter in consonants:
            consonants_count += 1
        elif letter != ' ' and letter not in russian_alphabet:
            wrong_letter = True

    if wrong_letter:
        print("Введены символы, не соответствующие русским буквам.")
    else:
        print(f"Количество гласных: {vowels_count}")
        print(f"Количество согласных: {consonants_count}")
        break



#Напишите программу, которая запрашивает у пользователя числа, вычисляет их сумму и среднее значение.
# Программа должна использовать циклы для обработки ввода и условные операторы для проверки корректности ввода.
while True:
    a = input("Введите число 1: ")
    b = input("Введите число 2: ")

    # Проверяем, что оба числа не пустые и состоят только из цифр
    this_number = True

    if len(a) == 0 or len(b) == 0:
        this_number = False
    else:
        # Проверяем число a
        for ch in a:
            if ch < '0' or ch > '9':
                this_number = False
                break
        # Если a прошёл проверку, проверяем b
        if this_number:
            for ch in b:
                if ch < '0' or ch > '9':
                    this_number = False
                    break

    if this_number:
        a = int(a)
        b = int(b)
        break
    else:
        print("Введите положительные числа")

sum_num = a + b
average_num = (a + b) / 2
print(f"Сумма равно {sum_num}")
print(f"Среднее значение равно {average_num}")



#Разработайте программу, которая запрашивает у пользователя число
# и выводит таблицу умножения для этого числа до 10.
while True:
    a = input("Введите целое положительное число: ")

    # Проверяем,строка не пустая и все цифры
    th_number = True
    if len(a) == 0:
        th_number = False
    else:
        for ch in a:
            if ch < '0' or ch > '9':  # если символ ввели
                th_number = False
                break

    if th_number:
        a = int(a)
        break
    else:
        print("Введите целое положительное число")

i = 1
while i <= 10:
    result = a * i
    print(f"{a} умножить на {i} равно {result}")
    i += 1

