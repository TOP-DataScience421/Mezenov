from pathlib import Path

def list_files(inp_path: str) -> '(*str) | None':
    """
    Функция принимает на вход путь к дирректории в виде str.
    Производит поиск файлов внутри переданной директории.
    Возвращает кортеж с именами найденных файлов, либо None, если файлов не будет найдено
    """
    
    path_to_parse = Path(inp_path)
    
    # Проверка на корректность переданного пути
    if not path_to_parse.is_dir():
        return None
    
    # Запускаем метод walk() класса Path
    for obj in path_to_parse.walk():
        # В первой итерации метод walk() возвращает кортеж из трех элементов, где третий элемент - это список названий файлов внутри головной (переданной) папки. Следующие итерации пойдут по внутренним подпапкам, поэтому обрываем выполнение с помощью return
        return tuple(obj[2])

# Ручные тесты функции:
# >>> print(list_files('C:\\LocalRepository\\Mezenov\\2024.05.15\\data'))
# ('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')
# >>> print(list_files('C:\\LocalRepository\\Mezenov\\2024.05.15\\data1'))
# None
# >>> print(list_files('C:\\LocalRepository\\Mezenov\\2024.05.15\\data\\c14KE'))
# ('5vsIh.dat', 'P2a91.dat')
# >>> print(list_files('C:\\LocalRepository\\Mezenov\\2024.05.15\\data\\mXbd9'))
# ('RoBjg.pt', 'z03EN.pt')
