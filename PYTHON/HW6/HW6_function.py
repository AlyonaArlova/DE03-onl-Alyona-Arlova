import ModuleforTask1 as ModuleforTask1
#1.Напишите функцию greet, которая принимает имя в качестве аргумента и выводит строку "Hello, [имя]!".

def greet(name):
    print(f"Hello, {name}!")

greet("Alyona")


#2. Напишите функцию add, которая принимает два числа и возвращает их сумму.
# Вызовите эту функцию с числами 5 и 3.

def add(a, b):
    return a + b
print(add(5, 3))

#3. Напишите модуль, содержащий функции для выполнения основных
# арифметических операций (сложение, вычитание, умножение, деление).
# Используйте этот модуль в другом файле для выполнения расчетов с различными числами
print(ModuleforTask1.add(3,4))
print(ModuleforTask1.substract(3,1))
print(ModuleforTask1.multiple(2, 3))