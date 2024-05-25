from datetime import datetime as dt
from pathlib import Path

def logger(func_obj: 'function') -> 'function':
    """Функция-декоратор. Выводит в консоль следующие параметры декорируемой функции:
    <название функции>(<*значения произвольного кол-ва позиционных аргументов через запятую>, <ключ = значение произвольного кол-ва ключевых элементов>) (-> <возвращаемое значение декорируемой функции>) ИЛИ ( .. <Названиие и описание любого перехваченного внутри декорируемой функции исключения>"""
   
    # Функция-обертка
    def wrapper(*args, **kwargs) -> 'any':
        
        # Относительный путь местоположения лог-файла
        log_file_path = Path('.\\data\\function_calls.log')
        call_time = dt.now()
        # Вносим название декорируемой функции в строку для вывода - logger_str
        logger_str = call_time.strftime('%Y.%m.%d %H:%M:%S') + ' — ' + str(func_obj.__name__) + '('
        n = 0
        
        # Сначала итеррируемся по позиционным и/или позиционно ключевым параметрам
        for n in range(0, func_obj.__code__.co_posonlyargcount): 
            # Пытаемся записать значения переданных аргументов в logger_str
            try:
                logger_str += str(args[n]) + ', '
            # Если вылетает исключение IndexError, значит следующие аргументы имеют стандартные значения, дописываем в logger_str стандартные значения
            except IndexError:
                logger_str += str(func_obj.__defaults__[n]) + ', '
        # Далее итеррируемся по ключевым аргументам
        for k in range(0, func_obj.__code__.co_kwonlyargcount): 
            # Записываем название ключа для текущей итеррации в переменную для удобства
            l_key = func_obj.__code__.co_varnames[k + n + 1]
            # Пытаемся записать значения переданных ключевых элементов в logger_str
            try:
                logger_str += str(l_key) + ' = ' + str(kwargs[l_key]) + ', '
            # Если вылетает исключение KeyError, значит следующие аргументы имеют стандартные значения
            except KeyError:
                logger_str += str(l_key) + ' = ' + str(func_obj.__kwdefaults__[l_key]) + ', '
        # Чтобы не усложнять код выше, вырезаем лишние символы после всех итерраций
        logger_str = logger_str.rstrip(', ') + ')'
        
        # Пытаемся вызвать декоррируемую функцию с произвольным набором аргументов
        try:
            logger_str += ' -> ' + str(func_obj(*args, **kwargs))
        # В случае врозникновения любого исключения, дописываем его название и описание в logger_str
        except Exception as exception:
            logger_str += ' .. ' + str(type(exception)).strip("<>class' ") + ': ' + str(exception)
        
        # Выводим в консоль получившуюся строку logger_str
        with open(log_file_path, 'a', encoding = 'utf-8') as f:
            print(logger_str, file = f)
    
    return wrapper
    
def divider(a: float | int = 1, b: float | int = 2, /, *, to_str = False, to_print = False) -> float | str | None:
    """
    Тестовая функция. Предназначена для проверки декоратора. Объявлена в тексте скрипта для удобства ручных проверок в консоли
    Делит два введенных числа друг на друга, либо возвращает число с плавающей точкой, либо печатает его в консоль
    """

    if to_str:
        c = str(a / b)
    else:
        c = a / b
        
    if to_print:
        print(c)
    else:
        return float(c)

divider = logger(divider)

# Ручные тесты функции:

# C:\LocalRepository\Mezenov\2024.05.15
# 0:10:10 > python -i 5.py
# >>> divider(4,5)
# >>> divider(4,5, to_str = True)
# >>> divider(4,5, to_print = True)
# 0.8
# >>> ^Z



# C:\LocalRepository\Mezenov\2024.05.15
# 0:10:25 > python -i 5.py
# >>> divider(4,5)

# Содержимое файла function_calls.log:

# 2024.05.24 00:10:12 — divider(4, 5, to_str = False, to_print = False) -> 0.8
# 2024.05.24 00:10:21 — divider(4, 5, to_str = True, to_print = False) -> 0.8
# 2024.05.24 00:10:23 — divider(4, 5, to_str = False, to_print = True) -> None
# 2024.05.24 00:10:30 — divider(4, 5, to_str = False, to_print = False) -> 0.8