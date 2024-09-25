'''
Файл содержит следующие конструкции для Лабораторной работы 3:
функция, вызывающая внутри себя другую функцию
функция, принимающая функцию как параметр (минимум 3 примера)
функция с объявленной внутри локальной функцией (минимум 2 примера)
'''
import random

def get_random_char():
    '''Возвращает случайный символ из списка'''
    chars = ['a', 'B', 'c', 'D', 'e', 'F', 1, 2.2]
    return random.choice(chars)


def get_type(char_fun):
    '''функция, принимающая функцию как параметр. Возвращает тип получаемого объекта'''
    return type(char_fun())


def make_uppercase(char_fun):
    '''функция, принимающая функцию как параметр. Делает букву заглавной'''
    inner_char = char_fun()
    def make_announcement_success(upper_char):
        print(f"Символ {inner_char} преобразован в заглавную букву {upper_char}")
    def make_announcement_failure():
        print(f"Переменная {inner_char} не подлежит преобразованию")
    if isinstance(inner_char, str):
        make_announcement_success(inner_char.upper())
        return inner_char.upper()
    else:
        make_announcement_failure()
        return inner_char


def make_lowercase(char_fun):
    '''функция, принимающая функцию как параметр. Делает букву прописной'''
    inner_char = char_fun()
    def make_announcement_success(upper_char):
        print(f"Символ {inner_char} преобразован в прописную букву {upper_char}")
    def make_announcement_failure():
        print(f"Переменная {inner_char} не подлежит преобразованию")
    if isinstance(inner_char, str):
        make_announcement_success(inner_char.lower())
        return inner_char.lower()
    else:
        make_announcement_failure()
        return inner_char


def create_code():
    '''функция, вызывающая внутри себя другую функцию. Возвращает 4-х значный буквенный код'''
    code = ""
    while len(code) < 4:
        char = get_random_char()
        if isinstance(char, str):
            code += char
    return code


def spelling_help(word):
    '''функция с объявленной внутри локальной функцией. Разделяет буквы в слове для удобства'''
    word_spelling = ""
    def format_change(char):
        return f"{char}-"
    for char in word:
        word_spelling += format_change(char)
    return word_spelling[:-1]


def birthdaty_info(day_of_birth, month_of_birth, age):
    '''функция с объявленной внутри локальной функцией. Выводит информацию о дне рождения'''
    def anniversary_check():
        if age % 5 == 0:
            print("Юбилей!")
    print(f"{day_of_birth}-го числа ({month_of_birth}) исполнится {age}.")
    anniversary_check()
