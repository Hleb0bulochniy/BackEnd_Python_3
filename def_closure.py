'''
Файл содержит следующие конструкции для Лабораторной работы 3:
функция с замыканиями (минимум 3 примера)
'''
def duplicate(char):
    '''функция дублирует строку заданное количество раз'''
    def inner(number):
        result = ""
        counter = 0
        while counter < number:
            counter += 1
            result += char
        return result
    return inner


def get_char_by_num(string):
    '''функция вовзращает n-ый символ строки'''
    def inner(num):
        return string[num-1]
    return inner


def code_check():
    '''функция проверяет совпадение кода и отправленной строки'''
    code = "qwerty"
    def inner(guess):
        if guess == code:
            return True
        else: return False
    return inner
