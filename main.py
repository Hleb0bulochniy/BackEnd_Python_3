'''
Файл содержит вызов конструкций для Лабораторной работы 3 в порядке:
функция без параметров
функция с параметрами
функция с несколькими параметрами со значениями по умолчанию
функция с несколькими параметрами, у которых задан тип
функция с неопределённым количеством параметров (args)
функция с неопределённым количеством параметров (kwargs)
функция, вызывающая внутри себя другую функцию
функция, принимающая функцию как параметр (минимум 3 примера)
функция с объявленной внутри локальной функцией (минимум 2 примера)
лямбда-выражение без параметров
лямбда-выражение с параметрами
функция, принимающая лямбда-выражение как параметр, и вызывающая лямбда-выражение внутри себя
функция с замыканиями (минимум 3 примера)
'''
from def_parametres import hello_world, divisibility, music_track, divisibility_typified
from def_parametres import parameter_args, parameter_kwargs

from def_inner_defs import get_random_char, get_type, make_lowercase, make_uppercase
from def_inner_defs import create_code, spelling_help, birthdaty_info

from def_lambda import execute_lambda, alert, alert_with_message

from def_closure import duplicate, get_char_by_num, code_check

if __name__ == '__main__':
    hello_world()
    print(divisibility(12,6))
    print(music_track())
    print(divisibility_typified(14,3))
    parameter_args("one", "two", "three")
    parameter_kwargs(name = "Daniil", surname = "Sashenkov")
    print("")
    print(get_type(get_random_char))
    print(make_uppercase(get_random_char))
    print(make_lowercase(get_random_char))
    print(create_code())
    print(spelling_help("Hello"))
    birthdaty_info(12, "Окт", 30)
    print("")
    execute_lambda(alert)
    execute_lambda(alert_with_message, "УГРОЗА!")
    print("")
    function = duplicate("a")
    print(function(4))
    function = get_char_by_num("qwertyuiop")
    print(function(3))
    function = code_check()
    print(function("qwerty"))
