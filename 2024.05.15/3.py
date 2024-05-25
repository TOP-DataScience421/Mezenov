from pathlib import Path
from importlib.util import spec_from_file_location
from importlib.util import module_from_spec
from utils import load_file
import sys

def ask_for_file() -> 'module':
    """
    Функция предназначена для поиска файла по заданному пользователем пути. После нахождения файла, копирует кго с помощью функции load_file() в папку из которой был вызван файл интерпретатором.
    Возвращает объект модуля, полученного из файла.
    """
    while True:
        path_to_look = Path(input('Введите путь к потерянному файлу: '))
        if path_to_look.exists() and path_to_look.is_file():
            break
        print('! по указанному пути отсутствует необходимый файл !')
        
    copied_file_path = load_file(path_to_look)
    module_name = copied_file_path.name.partition('.')[0]
    
    spec = spec_from_file_location(module_name, copied_file_path)
    module = module_from_spec(spec)

    sys.modules[module_name] = module
    
    spec.loader.exec_module(module)
    
    return module

# Примеры ручных тестов:
# >>> config_module = ask_for_file()
# Введите путь к потерянному файлу: C:\\LocalRepository\\Mezenov\\2024.05.15\\data\\conf1.py
# ! по указанному пути отсутствует необходимый файл !
# Введите путь к потерянному файлу: C:\\LocalRepository\\Mezenov\\2024.05.15\\data\\conf.py
# >>> config_module.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}
# >>> config_module
# <module 'conf' from 'C:\\LocalRepository\\Mezenov\\2024.05.15\\conf.py'>


    


    

    

    
    
    


    
