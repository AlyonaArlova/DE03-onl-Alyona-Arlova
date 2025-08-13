#Напишите программу, которая запрашивает у пользователя его возраст,
# преобразует введенное значение в целое число, добавляет к нему 5 и
# выводит сообщение: "Через 5 лет вам будет X лет", где X — рассчитанное значение.
age = input("Please enter your age: ")
if age.isdigit():
    age = int(age)
    if 0 < age <= 130:
        after5_age = age + 5
        print(f"Через 5 лет вам будет {after5_age} лет")
    else:
        print("Возраст должен быть от 1 до 130")
else:
    print("Ошибка: введите корректное число")


#Количество чётных и нечётных чисел в диапазоне Задача: Пользователь вводит числа a и b (a ≤ b).
# Вывести количество чётных и нечётных чисел в этом диапазоне
print("Please enter 2 numbers, so condition number1 <= number2 will be met")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Error: first number must be less than or equal to second number.")
else:
    even_count = 0
    odd_count = 0

    for number in range(a, b + 1):
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Number of even numbers:", even_count)
    print("Number of odd numbers:", odd_count)