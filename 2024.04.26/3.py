def math_function_resolver(math_func: 'function', *x: float | int, to_str_switch: bool = False):
    """Принимает объект математической функции <math_func> с единственным аргументом и применяет эту функцию к произвольному кол-ву аргументов <x>. 
    Возвращает список результатов каждого выполнения переданной математической функции в виде объектов str или int в зависимости от значения флага <to_str_switch>, передаваемого в качестве необязательного ключевого аргумента
    """
    result_list = []
    
    # Итерируемся по всем переданным аргументам. На каждой итерации применяем к математической функции текущий аргумент
    for v in x:
        # Записываем получившиеся значения в список сразу в нужном виде (int или str), чтобы минимизировать кол-во итераций по списку
        if to_str_switch:
            result_list.append(str(round(math_func(v))))
        else:
            result_list.append(round(math_func(v)))
    
    return result_list
    
def squared_x(x: float | int) -> float:
    return x*x
    
def rooted_x(x: float | int) -> float:
    return x**0.5
    
    
# Примеры ручных тестов:
# >>> math_function_resolver(lambda x: 5*x**2 - 0.5*x + 2, *range(1, 10), to_str_switch = True)
# ['6', '21', '46', '80', '124', '179', '244', '318', '402']
# >>> math_function_resolver(lambda x: 5*x**2 - 0.5*x + 2, *range(1, 10), to_str_switch = False)
# [6, 21, 46, 80, 124, 179, 244, 318, 402]
# >>> math_function_resolver(lambda x: 5*x**2 - 0.5*x + 2, *range(1, 10))
# [6, 21, 46, 80, 124, 179, 244, 318, 402]
# >>> math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
# [2, 1, 0, 0, 0, -1, -2, -2, -2]
# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# [2, 3, 4, 4, 4, 5, 6, 6, 6]
# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10), to_str_switch = True)
# ['2', '3', '4', '4', '4', '5', '6', '6', '6']
# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 20))
# [2, 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8, 8, 9, 10, 10, 10, 11, 12]
# >>> math_function_resolver(lambda x: 0.5*x + 2, *(1.5, 2.3 , 3.6 ,4.2  ,5.1 ,6.8 ,7), to_str_switch = True)
# ['3', '3', '4', '4', '5', '5', '6']
# >>> math_function_resolver(lambda x: 0.5*x + 2, *(1.5, 2.3 , 3.6 ,4.2  ,5 ,6 ,7))
# [3, 3, 4, 4, 4, 5, 6]
# >>> math_function_resolver(squared_x, *range(1, 10))
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# >>> math_function_resolver(rooted_x, *range(1, 10), to_str_switch = True)
# ['1', '1', '2', '2', '2', '2', '3', '3', '3']
# >>> math_function_resolver(rooted_x, *range(4, 100, 4), to_str_switch = True)
# ['2', '3', '3', '4', '4', '5', '5', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10']
# >>> math_function_resolver(rooted_x, *range(4, 100, 4))
# [2, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10]