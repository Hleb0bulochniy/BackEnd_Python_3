'''
Файл содержит следующие конструкции для Лабораторной работы 3:
функция без параметров
функция с параметрами
функция с несколькими параметрами со значениями по умолчанию
функция с несколькими параметрами, у которых задан тип
функция с неопределённым количеством параметров (args)
функция с неопределённым количеством параметров (kwargs)
'''


def hello_world():
    '''функция без параметров'''
    print("Hello, World!")


def divisibility(dividend, divisor):
    '''функция с параметрами'''
    if dividend % divisor == 0:
        return True
    return False


def music_track(author = "неизвестный", song = "неизвестно"):
    '''ункция с несколькими параметрами со значениями по умолчанию'''
    return f"{author} - {song}"


def divisibility_typified(dividend:int, divisor:int):
    '''функция с несколькими параметрами, у которых задан тип'''
    #типизация параметров работает, как аннотация при их вводе, а не как явное ограничение
    if dividend % divisor == 0:
        return True
    return False


def parameter_args(*args):
    '''функция с неопределённым количеством параметров (args)'''
    for item in args:
        print(item)


def parameter_kwargs(**kwargs):
    '''функция с неопределённым количеством параметров (kwargs)'''
    for key, value in kwargs.items():
        print(f"{key} - {value}")
