from collections.abc import Iterable
from numbers import Number
from typing import Self
import operator as op
from pprint import pprint

class Matrix:
    """
    Класс Matrix.
    Описывает матрицу чисел.
    Элементами матрицы могут быть объекты любого числового типа.

    Класс поддерживает следующие операции:
        - транспонирование
        - поэлементное сложение с другой матрицей и числом
        - поэлементное вычитания с другой матрицей и числом
        - поэлементное умножения на число
        - унарное отрицание
        - строковое представление матрицы с выравниванием столбцов

    Поля класса отсутствуют.

    Атрибуты экземпляра:
        __rows: list[list[Number]] - строки матрицы
        n: int - количество строк
        m: int - количество столбцов
        
    Свойства:
        transpose -> Self
            геттер - возвращает транспонированную матрицу
   
        
    Объявленные специальные методы:
        __init__()
        __getitem__()
        __add__()
        __radd__()
        __sub__()
        __rsub__()
        __mul__()
        __rmul__()
        __neg__()
        __repr__()
        
    """
    
    def __init__(self, raw_matrix: Iterable[Iterable[Number]]):
        self.__rows: list[Iterable[Number]] = []
        # Если сконструиировать матрицу невозможно, вызывае  прерывание
        if not Matrix.is_valid(raw_matrix):
            raise ValueError('Невозможно сконструировать матрицу.')
        
        # Конструируем матрицу
        for row in raw_matrix:
            self.__rows.append(list(row))
            
        self.n: int = len(self.__rows)
        self.m: int = len(self.__rows[0])
    
    
    @property
    def transpose(self) -> Self:
        """
        Свойство (геттер)
        Возвращает объет транспонированной матрицы от экземпляра матрицы, который ее вызвал
        """
        return Matrix([[y[x] for y in self.__rows] for x in range(self.m)])
        
    
    def __element_wise_operation(self, operation: callable, other: Self | Number = None) -> Self | None:
        """
        Функция высшего порядка
        Принимает объект мат. функции, экземпляр матрицы и экземпляр объекта с которым нужно провести мат. операцию
        Возвращает матрицу после проведения требуемой мат. операции
        """
        result: Matrix = Matrix(self.__rows)
        
        # Итерирруемся по строкам матрицы
        for row in range(self.n):
            # Итерируемся по элементам матрицы
            for ind in range(self.m):
                
                
                # Если проводим мат. операцию матрицы с числом
                if isinstance(other, Number):
                    result[row][ind] = operation(self[row][ind], other)
                # Если проводим мат. операцию матрицы с матрицей
                elif isinstance(other, Matrix):
                    if other.n == self.n and other.m == self.m:
                        result[row][ind] = operation(self[row][ind], other[row][ind])
                    else:
                        raise ValueError('Алгебраические операции возможны только с матрицами одной размерности.')
                elif other is None:
                    result[row][ind] = operation(self[row][ind])
                else:
                    raise TypeError('Алгебраические операции возможны только с матрицами и числами.')
                
        return result
        
    
    @staticmethod
    def is_valid(raw_matrix: Iterable[Iterable[Number]]) -> bool:
        """
        Статический метод класса
        Проверяет, является ли переданный аргумент подходящим объектом для конструирования матрицы
        Возвращает bool
        """
        valid_flag: bool = True
        
        # Проверка, что переданный объект - Iterable
        if isinstance(raw_matrix, Iterable):
            elem_count = len(raw_matrix[0])
            for row in raw_matrix:
                # Проверка, что строки переданного элемента - Iterable
                if not isinstance(row, Iterable) or elem_count != len(row):
                    valid_flag = False
                    break
                for elem in row:
                    # Проверка, что элементы строк - Number
                    if not isinstance(elem, Number):
                        valid_flag = False
                        break
        else:
            valid_flag = False
            
        return valid_flag
    
    
      
    def __getitem__(self, key: int) -> list[Number]:
        return self.__rows[key]
    
    def __add__(self, other: Self | Number) -> Self:
        return self.__element_wise_operation(op.add, other)
    
    def __radd__(self, other: Self | Number) -> Self:
        return self.__element_wise_operation(op.add, other)
        
    def __sub__(self, other: Self | Number) -> Self:
        return self.__element_wise_operation(op.sub, other)
    
    def __rsub__(self, other: Self | Number) -> Self:
        result = self.__element_wise_operation(op.neg)
        return result.__element_wise_operation(op.add, other)
        
    def __mul__(self, other: Self | Number) -> Self:
        if isinstance(other, Matrix):
            raise NotImplementedError('умножение матриц будет реализовано в будущем')
        return self.__element_wise_operation(op.mul, other)
    
    def __rmul__(self, other: Self | Number) -> Self:
        return self.__element_wise_operation(op.mul, other)
        
    def __neg__(self) -> Self:
        return self.__element_wise_operation(op.neg)
        
    def __repr__(self) -> str:
        output: str = ''
        max_elem_width: int = 0
        
        for row in self.__rows:
            for elem in row:
                max_elem_width = max(max_elem_width, len(str(elem)))
        
        for row in self.__rows:
            for elem in row:
                output += str(elem).rjust(max_elem_width) + ' '
            output = output + '\n' 
        
        return output.rstrip('\n')
        
# Ручные тесты:
# >>> Matrix([[1, 2], [1, 2, 3, 4]])
# ...
# ValueError: Невозможно сконструировать матрицу.
# >>> m1 = Matrix([[1, 1, 1], [1, 1, 1]])
# >>> m2 = Matrix([[3, 3, 3], [3, 3, 3]])
# >>>
# >>> m1
# 1 1 1
# 1 1 1
# >>>
# >>> m2
# 3 3 3
# 3 3 3
# >>>
# >>> for i in range(m1.n):
# ...     for j in range(m1.m):
# ...         print(m1[i][j], end=' ')
# ...
# 1 1 1 1 1 1 >>>
# >>>
# >>> m2.transpose
# 3 3
# 3 3
# 3 3
# >>>
# >>> m1 + m2
# 4 4 4
# 4 4 4
# >>>
# >>> m1 - m2
# -2 -2 -2
# -2 -2 -2
# >>>
# >>> m1 * m2
# ...
# NotImplementedError: умножение матриц будет реализовано в будущем
# >>>
# >>> 5 + m1
# 6 6 6
# 6 6 6
# >>> 10 - m2
# 7 7 7
# 7 7 7
# >>>
# >>> m1[0][2] = 7
# >>> m1[1][2] = 7
# >>>
# >>> m1
# 1 1 7
# 1 1 7
# >>>
# >>> m1.transpose
# 1 1
# 1 1
# 7 7
# >>>
# >>> m3 = Matrix([[1, 2], [3, 4]])
# >>>
# >>> m1 + m3
# ...
# ValueError: Алгебраические операции возможны только с матрицами одной размерности.
# >>>
# >>> m3 * 3.9
# 3.9  7.8
# 11.7 15.6
# >>>
# >>> -m3
# -1 -2
# -3 -4
# >>>
# >>> m3 + [2,1,3]
# ...
# TypeError: Алгебраические операции возможны только с матрицами и числами.
        


