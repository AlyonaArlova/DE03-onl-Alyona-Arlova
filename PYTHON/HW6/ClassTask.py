# Напишите программу, которая запрашивает у пользователя
#ввод числа и выполняет деление 100 на это число. Обработайте
#возможные исключения, такие как деление на ноль и ввод
#нечислового значения.
print("TASK 1")
try:
    number = float(input("Enter int number: "))
    division = 100 / number
    print(f"Our division result is: 100 / {number} = {division}")
except ZeroDivisionError:
    print("Not acceptable: Zero Division!")
except ValueError:
    print("Please enter only numbers!")

#Напишите программу, которая запрашивает у пользователя
#ввод числа, проверяет его на положительное значение,
#используя пользовательское исключение, и выводит результат.
print("TASK 2")
class CheckIfNumberNegative(Exception):
    pass
def check_num(number):
    if user_input < 0:
        raise CheckIfNumberNegative("Error: Number should be > 0")
    else:
        print(f"Your number is {user_input} and it's positive!")
try:
    user_input = float(input("Enter int number: "))
    check_num(5)
except ValueError:
    print("Please enter only numbers!")
except CheckIfNumberNegative as e:
    print(e)

#Написать программу, которая запрашивает у пользователя число и выводит его квадрат.
# Обработать случай, если введено не число.
print("TASK 3")
try:
    square_number = float(input("Enter int number: "))
    print(f"Square of the number is: {square_number ** 2} ")

except ValueError:
    print("Please enter only numbers!")

#Создать класс собственного исключения TooSmallError,
# которое возникает, если число меньше 10.
print("TASK 4")
class TooSmall(Exception):
    pass
try:
    any_number = float(input("Enter int number: "))
    if any_number < 10:
        raise TooSmall("Number is less than 10")
except ValueError:
    print("Please enter only numbers!")
except TooSmall as e:
    print(e)