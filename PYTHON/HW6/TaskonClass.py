#1. Считайте с клавиатуры пять чисел, сохраните их в список и выведите только те,
# которые больше 10.
lst = []
for i in range(5):
    a = input("Enter number ")
    if a.isdigit():
        lst.append(int(a))
    else:
        print("You should enter digits")
for i in lst:
    if i > 10:
        print(i)
else:
    print("All numbers are less than 10")

# 2. Считайте с клавиатуры любое количество чисел до тех пор, пока пользователь не введёт 0.
# Сохраните все введённые числа в файл numbers.txt.
filetxt = r"PYTHON/HW6/filefornumber.txt"
try:
    with open(filetxt,'w+') as F:
        while True:
            b = input("Enter number ")
            if b == '0': break
            elif b.isdigit():
               F.write(f"{b}\n")
            else:
                print("You should enter digits")

except FileNotFoundError:
    print("Issue with doc")
except IsADirectoryError:
    print("Issue with doc")
except FileExistsError:
    print("Issue with doc")
finally:
    print("Finish of execution")


# 3. Считайте с клавиатуры десять чисел, сохраните их в список,
# отберите только чётные и запишите их в файл even.txt.
# Затем прочитайте файл и выведите содержимое на экран.
evenfile = r"PYTHON/HW6/even.txt"

try:
    with open(evenfile, 'w+') as E:
        for i in range(10):
            c = input("Enter number: ").strip()
            try:
                num = int(c)
                if num % 2 == 0:
                    E.write(str(num) + "\n")
                else:
                    print("Number is not even")
            except ValueError:
                print("You should enter digits")

        E.seek(0)
        print("Even numbers in file:")
        print(E.read())

except FileNotFoundError:
    print("Issue with doc")
except IsADirectoryError:
    print("Issue with doc")
except FileExistsError:
    print("Issue with doc")
finally:
    print("Finish of execution")
