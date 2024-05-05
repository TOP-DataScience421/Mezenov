def deck():
    """Функция-генератор. На каждой итерации возвращает кортеж из номинала карты и масти, пока не вернет всю колоду"""
    # Создаем список названий мастей для удобного к ним обращения
    suits_list = ['червы', 'бубны', 'пики', 'трефы']
    
    # Итеррируемся по названиям мастей
    for s in suits_list:
        # Итеррируемся по номиналам карт
        for c in range(2, 15):
            # В очередном вызове возвращаем кортеж из текущего номинала карты и названия масти
            yield c, s

# Примеры ручных тестов:
# >>> list(deck())[::]
# [(2, 'червы'), (3, 'червы'), (4, 'червы'), (5, 'червы'), (6, 'червы'), (7, 'червы'), (8, 'червы'), (9, 'червы'), (10, 'червы'), (11, 'червы'), (12, 'червы'), (13, 'червы'), (14, 'червы'), (2, 'бубны'), (3, 'бубны'), (4, 'бубны'), (5, 'бубны'), (6, 'бубны'), (7, 'бубны'), (8, 'бубны'), (9, 'бубны'), (10, 'бубны'), (11, 'бубны'), (12, 'бубны'), (13, 'бубны'), (14, 'бубны'), (2, 'пики'), (3, 'пики'), (4, 'пики'), (5, 'пики'), (6, 'пики'), (7, 'пики'), (8, 'пики'), (9, 'пики'), (10, 'пики'), (11, 'пики'), (12, 'пики'), (13, 'пики'), (14, 'пики'), (2, 'трефы'), (3, 'трефы'), (4, 'трефы'), (5, 'трефы'), (6, 'трефы'), (7, 'трефы'), (8, 'трефы'), (9, 'трефы'), (10, 'трефы'), (11, 'трефы'), (12, 'трефы'), (13, 'трефы'), (14, 'трефы')]
# >>> list(deck())[::13]
# [(2, 'червы'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]
# >>> list(deck())[::2]
# [(2, 'червы'), (4, 'червы'), (6, 'червы'), (8, 'червы'), (10, 'червы'), (12, 'червы'), (14, 'червы'), (3, 'бубны'), (5, 'бубны'), (7, 'бубны'), (9, 'бубны'), (11, 'бубны'), (13, 'бубны'), (2, 'пики'), (4, 'пики'), (6, 'пики'), (8, 'пики'), (10, 'пики'), (12, 'пики'), (14, 'пики'), (3, 'трефы'), (5, 'трефы'), (7, 'трефы'), (9, 'трефы'), (11, 'трефы'), (13, 'трефы')]
# >>> list(deck())[::14]
# [(2, 'червы'), (3, 'бубны'), (4, 'пики'), (5, 'трефы')]
# >>> list(deck())[0:10:14]
# [(2, 'червы')]
# >>> list(deck())[12:0:-1]
# [(14, 'червы'), (13, 'червы'), (12, 'червы'), (11, 'червы'), (10, 'червы'), (9, 'червы'), (8, 'червы'), (7, 'червы'), (6, 'червы'), (5, 'червы'), (4, 'червы'), (3, 'червы')]