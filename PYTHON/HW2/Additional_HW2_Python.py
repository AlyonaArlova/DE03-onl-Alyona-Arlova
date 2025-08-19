#Калькулятор: Напишите программу, которая выполняет простейшие арифметические
#операции (сложение, вычитание, умножение, деление) между двумя числами в
#зависимости от выбора пользователя. Используйте условные операторы if-elifelse для обработки выбора операции

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

while True:
    c = input("Select operator: Addition - enter 1; Subtraction - enter 2; Division - enter 3; Multiplication - enter 4: ")

    if c == '1':
        print("A + B = ", a + b)
        break
    elif c == '2':
        print("A - B = ", a - b)
        break
    elif c == '3':
        if b == 0:
            print("Cannot divide by zero.")
        else:
            print("A / B = ", a / b)
            break
    elif c == '4':
        print("A * B = ", a * b)
        break
    else:
        print("Enter a value from the proposed list (1, 2, 3, 4)")


#Числа Фибоначчи: Напишите программу, которая выводит первые 10 чисел
a = 0
b = 1

for i in range(10):
    print("Fibonacci number:", a) #  current number

    next_number = a + b # calc  next Fibonacci number
    a = b               # move b into a
    b = next_number

#Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
#По данному натуральному n вычислите значение n!
n = int(input("Введите n: "))
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print(f"{n}! =", factorial)