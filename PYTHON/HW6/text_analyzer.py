#5.Создайте программу в модуле main.py, которая использует функцию analyze_file(path) из
# модуля text_analyzer.py.
# Функция считывает содержимое указанного текстового файла, определяет количество строк,
# количество слов и самое длинное слово, а затем возвращает эти данные в виде строки.
# Программа выводит результат в консоль и сохраняет его в файл analysis.txt.
def analyze_file(path):
    try:
        with open(path, 'r') as myfavfile:
            content = myfavfile.read()
            print("количество строк в заданном текстовом файл: ", len(content.splitlines()) )
            print("количество слов в заданном текстовом файл:", len(content.split()))
            result = f"Количество строк: {len(content.splitlines())}, Количество слов: {len(content.split())}, Самое длинное слово: '{max(content.split(), key=len)}'"
            return result
    except FileNotFoundError:
        return "Файл не найден"
    except Exception as e:
        return f"Произошла ошибка: {e}"