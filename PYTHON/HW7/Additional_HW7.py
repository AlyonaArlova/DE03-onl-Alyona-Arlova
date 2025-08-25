#Дополнительное задание:
#1. Создайте программу, которая запрашивает у пользователя список чисел,
#введённых через пробел, и сохраняет их в список; напишите функцию,
# которая перебирает этот список в цикле и вычисляет квадрат каждого числа,
#но если встречается отрицательное число, выбрасывается собственное исключение
# NegativeNumberError с сообщением «Отрицательные числа недопустимы», при этом программа должна обработать это
# исключение, вывести сообщение об ошибке и продолжить обработку остальных элементов, а в
# конце вывести итоговый список квадратов всех корректных чисел.
print("TASK 1")
class NegativeNumberError(Exception):
    pass
numbers = input("Введите числа: ").split()
new_list = []
for i in numbers:
    try:
        num = int(i)
        if num < 0:
            raise NegativeNumberError("Отрицательные числа недопустимы")

        else:
            new_list.append(num ** 2)
    except ValueError:
        print("Check the user input, should be only numbers", {i})
    except NegativeNumberError as e:
        print("Error:", e, num)

print("Task execution is done")
print("итоговый список квадратов всех корректных чисел", new_list)


#2. Создайте программу, которая запрашивает у пользователя пары «ключ:значение», введённые через запятую,
# и сохраняет их в словарь; напишите функцию, которая в цикле проходит по словарю и проверяет, чтобы все значения
# были положительными числами, при этом если встречается отрицательное число или строка вместо числа,
# выбрасывается собственное исключение InvalidValueError с сообщением «Некорректное значение для ключа <ключ>»,
# программа должна обработать это исключение, вывести предупреждение и продолжить проверку остальных элементов,
# а в конце вывести словарь только с корректными данными.
print("TASK 2")
class InvalidValueError(Exception):
    pass

raw_input = input("введите пары «ключ:значение» через запятую: ").split(",")
new_dct = {}

for g in raw_input:
    g.strip()
    key, value = g.split()
    new_dct[key] = value

def check_dct(new_dct):
    valid_dct = {}
    for key, value in new_dct.items():
        try:
            num = int(value)  # преобразовать значение в число
            if num < 0:
                raise InvalidValueError(f"Некорректное значение для ключа {key}")
            valid_dct[key] = num  # добавляем только корректные значения
        except ValueError:
            print(f"Некорректное значение для ключа {key}")
        except InvalidValueError as e:
            print(e)
    return valid_dct


valid_dct = check_dct(new_dct)
print("Корректные данные:", valid_dct)


#3. Создайте программу, которая запрашивает у пользователя число и с помощью цикла считает факториал этого числа,
# при этом если пользователь вводит отрицательное значение, должно выбрасываться собственное исключение
# NegativeFactorialError с сообщением «Факториал отрицательных чисел не определён», программа должна обработать
# это исключение и вывести сообщение об ошибке, а при корректном вводе — напечатать результат вычисления
# факториала.
print("TASK 3")
class NegativeFactorialError(Exception):
    pass
enter_number = int(input("Введите число: "))
start = 1
try:
    if enter_number < 0:
        raise NegativeFactorialError("Факториал отрицательных чисел не определён")
    for i in range(1, enter_number+1):
        start = start * i
    print(f"Factorial {enter_number} is {start}")
except NegativeFactorialError as e:
    print("Error:", e)
