#Создайте переменную x и присвойте ей значение 10. Выведите значение переменнойна экран.
x = 10
print(x)

#Создайте переменные name (строка), age (число) и is_student (булевый тип). Выведите их значения
name = "Alyona"
age = 35
is_student = False
print(f"My name is {name}. I am {age}. Am I student? {is_student}")

#Напишите программу,
# которая запрашивает у пользователя три числа, сравнивает их между собой
# и выводит максимальное и  минимальное число
# Запрос чисел у пользователя
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

# Вычисление максимума и минимума
max_number = max(a, b, c)
min_number = min(a, b, c)
if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c
if a <= b and a <= c:
    min_num = a
elif b <= a and b <= c:
    min_num = b
else:
    min_num = c

# Вывод результата
print("Maximum number is:", max_number)
print("Maximum number is:", max_num)
print("Minimum number is:", min_number)
print("Minimum number is:", min_num)