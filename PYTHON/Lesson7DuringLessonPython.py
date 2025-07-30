#Подсчет количества гласных в строке
word = input("Введите слово: ").lower()
vowels = ['a','е','ё','и','о','у','ы','э','ю','я']  # Русские гласные

count = 0
for letter in word:
    if letter in vowels:
        count += 1

print(f"Количество гласных: {count}")

#Проверка четности числа
a=int(input("Enter number: "))
if a % 2 == 0:
    print("Число четное")
else:
    print("Нечетное число")

#Напишите программу, которая находит наибольшее из трех чисел: 3, 7 и 5.
# Программа должна выводить максимальное число.
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))
max_number= max(a,b,c)
print(max_number)

