#Что нужно сделать дома?
#1.Напишите функцию, которая принимает список чисел и возвращает их среднее значение. Обработайте исключения,
# связанные с пустым списком и некорректными типами данных.
class EmptyList(Exception):
    pass

def process_numbers():
    try:
        input_str = input("Please enter any number separated by space: ")
        part_of_string = input_str.split()
        numbers = [float(x) for x in part_of_string]

        if len(numbers) == 0:
            raise EmptyList("Empty list is not allowed")

        print("Min number: ", min(numbers))
        print("Max number: ", max(numbers))
        print("Average: ", sum(numbers) / len(numbers))

    except ValueError:
        print("Please enter only numbers")
    except EmptyList as e:
        print(f"Error: {e}")

process_numbers()




#2. Создайте программу, которая считывает список чисел из файла, проверяет каждое число на чётность и записывает
# результаты (чётное или нечётное) в другой файл. Используйте обработку исключений для возможных ошибок
# ввода-вывода.
inputFile = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/HW6/input_file.txt"
outputFile = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/HW6/output_file.txt"
def check_file_numbers(inputFile, outputFile):
    try:
        with open(inputFile, 'r') as infile:
            lines = infile.readlines()

        with open(outputFile, "w") as outfile:
            for line in lines:
                try:
                    num = int(line.strip())
                    if num % 2 == 0:
                        outfile.write(f"Even number: {num}\n")
                    else:
                        outfile.write("Odd number: " + str(num) + "\n")
                except ValueError:
                    outfile.write("Invalid entry: " + line)

    except FileNotFoundError:
        print(f"Error: file {inputFile} not found")
    except IOError as e:
        print(f"IO error: {e}")
    finally:
        print("Execution of task 2 is done!")

check_file_numbers(inputFile, outputFile)



