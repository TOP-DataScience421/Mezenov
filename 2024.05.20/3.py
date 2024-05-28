
class ChessKing:
    """
    Класс ChessKing.
    Описывает шахматную фигуру короля.
    
    Атрибуты экземпляра:
        color: str - цвет фигуры
        square: str - поле шахматной доски, на котором в данный момент находится фигура
    
    Методы:
        __init__()
        __repr__()
        __str__()
        
        __get_instance_name() -> '__instance__.name'
            защищенный метод класса. Предназначен для поиска имени экземпляра класса, который его вызвал
        is_turn_valid() -> bool
            принимает на вход строку нового поля и проверяет, возможен ли для данной фигуры ход с текущего поля на новое
        turn() -> None
            принимает на вход строку нового поля и выполняет ход, выбрасывает ValueError в случае невозможности выполнить ход
    """
    
    # Поля класса. 
    # Словарь соответствий буквенных индексов цифрами от 1 до 8
    files = {chr(c): c - ord('A') + 1 for c in range(ord('A'), ord('H')+1)}
    # Словарь соответствий численных индексов (в формате строки) цифрами от 1 до 8
    ranks = {str(n): n for n in range(1, 9)}
    
    def __init__(self, color: str = 'white', square: str = None):
        # Проверяем формальные признаки. Длину переданного индекса клетки, правильность самих переданных символов
        if not (square is None) and len(square) == 2 and square[0].upper() in self.files.keys() and square[1] in self.ranks.keys():
            # Для исключения путанницы, все введенные индексы переводим в верхний регистр
            self.square = square.upper()
            # Вычисляем цвет клетки 
            if self.files[self.square[0]] % 2 == self.ranks[self.square[1]] % 2:
                self.color = 'black'
            else:
                self.color = 'white'
        else:
            # Записываем стандартное положение, если таковое не было передано или было передано неправильно
            self.square = 'E8'
            self.color = 'white'
        
       
    def __str__(self):
        return f'{self.__get_instance_name()}: {self.square}'
    
    def __repr__(self):
        return f"'{self.__get_instance_name()}: {self.square}'"
        
            
    def __get_instance_name(self):
        """
        Дополнительный защищенный метод.
        Возвращает название экземпляра из которого был вызван.
        """
        # В глобальном словаре имен объектов ищем совпадение по названию экземпляра и возвращаем его
        for k, v in globals().items():
            if v is self:
                return k
        
    def is_turn_valid(self, new_cell: str) -> bool:
        """
        Метод класса
        Принимает на вход строку нового поля и проверяет, возможен ли для данной фигуры ход с текущего поля на новое
        """
        new_cell = new_cell.upper()
        # Ход возможен, если любой из переданных индексов меняется не больше чем на 1, так же считаем, что на месте король остаться не может
        if self.files[new_cell[0]] - self.files[self.square[0]] > 1 or self.ranks[new_cell[1]] - self.ranks[self.square[1]] > 1 or self.square == new_cell:
            return False
        return True
        
    def new_turn(self, new_cell: str) -> None:
        """
        Метод класса
        Принимает на вход строку нового поля и выполняет ход, выбрасывает ValueError в случае невозможности выполнить ход
        """
        new_cell = new_cell.upper()
        # Проверяем формальные параметры новой клетки для хода - длину строки, правильность букв/цифр
        if len(new_cell) == 2 and new_cell[0] in self.files.keys() and new_cell[1] in self.ranks.keys():
            
            # Если ход возможен меняем текущее положение короля на переданное
            if self.is_turn_valid(new_cell):
                self.square = new_cell
                # Вычисляем цвет новой клетки
                if self.files[self.square[0]] % 2 == self.ranks[self.square[1]] % 2:
                    self.color = 'black'
                else:
                    self.color = 'white'
                return None
        # Если добрались сюда, значит ввод клетки неккоректный, либо такой ход невозможен.Выбрасываем ValueError Exception
        raise ValueError
        
        
# Ручные тесты:
# >>> WK = ChessKing()
# >>> WK
# 'WK: E8'
# >>> print(WK)
# WK: E8
# >>> WK.new_turn('E7')
# >>> WK.new_turn('D6')
# >>> WK.color
# 'black'
# >>> WK
# 'WK: D6'
# >>> WK.new_turn('D5')
# >>> WK.color
# 'white'
# >>> WK = ChessKing('E1')
# >>> WK
# 'WK: E8'
# >>> WK = ChessKing(square = 'E1')
# >>> WK
# 'WK: E1'
# >>> WK.color
# 'black'
# >>> WK
# 'WK: E1'
# >>> WK.new_turn('A8')
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
  # File "C:\LocalRepository\Mezenov\2024.05.20\3.py", line 95, in new_turn
# ValueError
# >>> WK.new_turn('D2')
# >>> WK
# 'WK: D2'
# >>> WK.color
# 'black'

        
    
    