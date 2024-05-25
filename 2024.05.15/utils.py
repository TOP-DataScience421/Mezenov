"""
Модуль Utils.
Содержит функции:
important_message() - используется для вывода сообщения в предустановленной рамке
stripped_msg_gen() - используется функцией important message() для реализации ее работы. Не предназначена для внешнего использования
load_file() - функция предназначенная для копированния файла
search_infile_for() - функция ищет в файле ключевое слово
Вспомогательные функции для игры историческая Викторина:
print_header() - печатает приветственное сообщение игроку
questions_file_parser - предназначена для выделения в удобную структуру вопросов и ответов для викторины из файла
check_answer() - предназначена для проверки правильности ответа игрока и вычисления времени затраченного на ответ
score_calc() - вычисляет сколько игрок заработал очков в текущем раунде
"""

from shutil import get_terminal_size

def important_message(inp_str: str) -> str:
    """
    Функция принимает строку и возвращает эту строку обрамленную рамкой предустановленного формата
    """
    
    columns = get_terminal_size()[0]
    result_msg = ''
    
    # Построчный набор сообщения для возврата из функции
    for str_obj in stripped_msg_gen(inp_str, columns):
        result_msg += str_obj
    
    return result_msg



def stripped_msg_gen(
                    inp_str: str, 
                    width: int,
                    *,
                    Up_Border: str = '=',
                    Left_Border: str = '#',
                    Right_Border: str = '#',
                    Down_Border: str = '=',
                    Fill_chr: str = ' '
                    ) -> str:
    """
    Функция-генератор. 
    Принимает строку и ширину в которую эту строку нужно вписать. Также принимает необязательные символы конструкции рамки, из которых она (рамка) будет построена вокруг введенного сообщения
    При каждой итерации будет построчно возвращать переданную на вход строку, вписанную в заданную рамку
    """

    inp_list = inp_str.split()
    stripped_msg = inp_list[0]
    
    # Верхняя часть рамки
    yield Left_Border + Up_Border * (width - 3) + Right_Border + '\n'
    yield Left_Border + Fill_chr  * (width - 3) + Right_Border + '\n'
    
    # Итерируемся по словам из переданной строки
    for i in range(len(inp_list)):
        
        # Ловим выход за пределы списка. Это обработка последнего слова из строки
        try:
            stripped_msg += ' ' + inp_list[i+1]
        except IndexError:
            yield Left_Border + stripped_msg.center(width - 3, Fill_chr) + Right_Border + '\n'
            
        # Если текущая набранная строка больше заданной ширины, то возвращаем полученную строку       
        if len(stripped_msg) > (width - 7):
            yield Left_Border + stripped_msg.rstrip(inp_list[i+1]).center(width - 3, Fill_chr) + Right_Border + '\n'
            # Начинаем набор строки для вывода со след. слова в новой итерации генераторной функции
            stripped_msg = inp_list[i+1]
    
    # Нижняя часть рамки
    yield Left_Border + Fill_chr    * (width - 3) + Right_Border + '\n' 
    yield Left_Border + Down_Border * (width - 3) + Right_Border + '\n'



from shutil import copy2
from pathlib import Path
from sys import path

    
def load_file(file_path: str | Path) -> Path:
    """
    load_file() - функция предназначенная для копированния файла из переданного ей на вход пути в путь корня файл из которого функция была вызвана. Возвращает путь к скопированному файлу
    """
    
    file_path = Path(file_path) if type(file_path) == str else file_path
    path_to_return = Path(path[0])
    
    copy2(file_path, path_to_return)
    
    return path_to_return / file_path.name   


from collections import deque   
from pprint import pprint


def search_infile_for(file_path: Path, file_name: str, word_for_search: str, context: int) -> dict:
    """
    Функция для поиска в текстовом файле по переданному пути ключевого слова с учетом глубины контекста
    Возвращает список словарей заданного формата
    """

    line_counter = 0
    result_list = []
    # Объявляем тип данных "очередь", для реализации движения по тексту "окном", с максимальной длиной зависящей от заданного context
    text_deque = deque('', 1 + context * 2)

    # Открываем переданный файл
    with open(file_path / file_name, 'r', encoding = 'utf-8') as f:
        
        # Считываем первыую строку из файла
        string = f.readline()
        
        # Итерируемся по строкам файла, пока они не кончатся
        while string:
            # На каждой итерации добавляем в конец очереди строку
            text_deque.append(string)
            # Формируем из текущей очереди текст для сравнения с ключевым словом
            text = '\n'.join(text_deque)
            line_counter += 1
            line_for_return = line_counter - context 
            
            # Считываем новую строку
            string = f.readline()
            
            # Проверка на то, что очередь (включачая контекст) первично набралась
            if line_for_return >= 1:
                
                # Ищем ключевое слово в текущем окне проверки (очереди)
                if word_for_search.lower() in text_deque[context].lower():
                
                    # Добавляем в список для возврата очередной словарь со всеми необходимыми параметрами
                    result_list.append({'keyword'   : word_for_search,
                                        'filename'  : file_name,
                                        'line'      : line_for_return,   
                                        'context'   : context,
                                        'text'      : text
                                        })
                                        
        # Блок "else" Для цикла "while", чтобы допройти элементы в конце очереди (выбрать контекст)
        else:
            
            # Пока не уменьшим длину очереди в половину, двигаемся к концу очереди
            while len(text_deque) > 1 + context:
                text_deque.popleft()
                text = (' '.join(text_deque))
                line_for_return += 1
                
                if word_for_search.lower() in text_deque[context].lower():

                    result_list.append({'keyword'   : word_for_search,
                                        'filename'  : file_name,
                                        'line'      : line_for_return,   
                                        'context'   : context,
                                        'text'      : text
                                        })
      
    return result_list
                
            
            



# Вспомогательные функции для реализации игры Блиц-Викторина
def print_header(header_msg: str, help_msg: str, prompt_msg: str) -> None:
    """
    Функция печатает приветственное сообщения игры Викторина. 
    Принимает на вход сообщения для печати в консоль и вид строки приглашения
    """

    print(important_message(header_msg))
    print(help_msg, end = '\n\n')
    input(prompt_msg)
    
    
def questions_file_parser(file_path: Path) -> dict:
    """
    Функция предназначена для преобразования списка вопросов-ответов из файла в структуру данных удобную для работы. Принимает на вход путь к файлу. Возвращает словарь вопросов-ответов
    """
    result_dict = dict()
    corresp_table = dict()
    answer = question = ''
    question_counter = 1
    
    with open(file_path, 'r', encoding = 'utf-8') as f:
        # Парсим файл построчно
        line = f.readline().rstrip('\n')
        
        while line:
            
            # Если первый символ в строке это цифра, значит это вариант ответа
            if line[0].isnumeric():
                answer = line.rstrip('\n')
                result_dict[question][answer.rstrip('\n+ ')] = answer.endswith('+')
            # Если не цифра, значит это вопрос
            else:
                if line != '\n':
                    question = line.rstrip('\n')
                    result_dict[question] = dict()
                    # составляем дополнительную таблицу соответствий номеров вопросов тексту вопроса
                    corresp_table[question_counter] = question
                    question_counter += 1
            line = f.readline()
            
    
    return result_dict, corresp_table
            
from time import perf_counter
    
def check_answer(right_num: int, msg_tbl: {str: str}) -> (bool, int):
    """
    Функция проверяет правильность ответа пользователя и выводит в консоль сообщения из списка текстов в зависимости от ответов. Возвращает кортеж из bool и int, где bool - правильный/неправильный ответ, int - время затраченное на ответ
    """
    result = False
    
    # Запускаем таймер, для отсчета времени на ответ
    start_time = perf_counter()
    
    while True:
        # Ждем ответа от игрока
        player_answer = input(msg_tbl[0])
        if player_answer.isnumeric():
            # Останавливаем таймер
            end_time = perf_counter()
            # Записываем в результат bool переменную где True - правильный ответ, а False - неправильный
            result = int(player_answer) == right_num
            # Возвращаем кортежем bool правильный/неправильный ответ и int время затраченное на ответ
            return result, int(end_time - start_time)
        else:
            # Введена не цифра, возвращаемся к запросу на новый ввод от игрока, выводим сообщение в консоль о неправильном вводе
            print(*msg_tbl[1:4], sep = '')
        
def score_calc(player_answer: bool, time_for_answer: int, time_limit: int, scores_tbl: list[int], info_tbl: {str: str}) -> int:
    """
    Функция принимает факт правильности/неправильности ответа игрока, время затраченное на ответ и таблицы констант для подсчета очков и текстовых сообщений для вывода в консоль в зависимсоти от ситуации.
    Возвращает кол-во очков за текущий ответ
    """

    result = info_tbl[6]
    
    # Если ответ игрока верный
    if player_answer:
        # Если игрок уложился в лимит времени, выводим в консоль сообщение о правильном ответе, возвращаем результат очков из таблицы соответствующее правильному и быстрому ответу
        if time_for_answer <= time_limit:
            result = info_tbl[4]
            score = scores_tbl[0]
        # Если игрок не уложился в лимит времени, выводим в консоль сообщение о правильном ответе, возвращаем результат очков из таблицы соответствующее правильному и медленному ответу
        else:
            result = info_tbl[5]
            score = scores_tbl[1]
        print(result + f' ({time_for_answer}) сек' + '\n')
    # Если игрок дал неправильный ответ, выводим в консоль сообщение о неправильном ответе, возвращаем результ очков из таблицы соответствующее неправильному ответу
    else:
        print(result, '\n')
        score = scores_tbl[2]
    return score    
    
    