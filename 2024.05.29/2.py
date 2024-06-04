from collections.abc import Iterable
from numbers import Number
from typing import Self
import operator as op
from pprint import pprint
from functools import cached_property
from functools import cache

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
        __flat: tuple[Number, ...] - элементы матрицы в порядке: числа первой строки, числа второй строки, ...
        n: int - количество строк
        m: int - количество столбцов
        __transpose: Iterable[Number] - элементы матрицы в порядке: числа первого столбца, числа второго столбца, ... 
        
    Свойства:
        transpose -> Self
            геттер - возвращает транспонированную матрицу
   
        
    Объявленные специальные методы:
        __init__()
        __add__()
        __radd__()
        __sub__()
        __rsub__()
        __mul__()
        __rmul__()
        __neg__()
        __repr__()
        
    """
    
    def __init__(self, *raw_matrix: Number, n: int, m: int):
        
        
        self.__flat = raw_matrix
        # Если сконструиировать матрицу невозможно, вызывает  прерывание
        if not Matrix.is_valid(list(self.__flat), n, m):
            raise ValueError('Невозможно сконструировать матрицу.')
        
        self.n = n
        self.m = m
        
        self.__transpose = []
        
        for r in range(self.m):
            for c in range(0, len(self.__flat), self.m):
                self.__transpose.append(self.__flat[c+r])
        
        self.__transpose = tuple(self.__transpose)
       
        
    
    
    @cached_property
    def transpose(self) -> Self:
        """
        Свойство (геттер)
        Кэшировано
        Возвращает объет транспонированной матрицы от экземпляра матрицы, который ее вызвал.
        """
                       
        return Matrix(*self.__transpose, n = self.m, m = self.n)
        
    
    def __element_wise_operation(self, operation: callable, other: Self | Number = None) -> Self | None:
        """
        Функция высшего порядка
        Принимает объект мат. функции, экземпляр матрицы и экземпляр объекта с которым нужно провести мат. операцию
        Возвращает матрицу после проведения требуемой мат. операции
        """
        result = list(self.__flat)
        
        # Итерирруемся по строкам матрицы
        for ind in range(len(self.__flat)):
                   
            # Если проводим мат. операцию матрицы с числом
            if isinstance(other, Number):
                result[ind] = operation(self.__flat[ind], other)
            # Если проводим мат. операцию матрицы с матрицей
            elif isinstance(other, Matrix):
                if other.n == self.n and other.m == self.m:
                    result[ind] = operation(self.__flat[ind], other.__flat[ind])
                else:
                    raise ValueError('Алгебраические операции возможны только с матрицами одной размерности.')
            else:
                raise TypeError('Алгебраические операции возможны только с матрицами и числами.')
                
        return Matrix(*result, n = self.n, m = self.m)
        
    
    @staticmethod
    def is_valid(processed_matrix: list[Number], n: int, m: int) -> bool:
        """
        Статический метод класса
        Проверяет, является ли переданный аргумент подходящим объектом для конструирования матрицы
        Возвращает bool
        """
        valid_flag = True
        
        # Проверка, что переданный объект - Iterable
        if isinstance(processed_matrix, Iterable) and isinstance(n, int) and isinstance(m, int):
            # print('Прошли проверку Iterable, int, int')
            elem_count = len(processed_matrix)
            # Проверка корректности длины матрицы
            if elem_count == m * n:
                # print('Прошли проверку длины')
                for elem in processed_matrix:
                    # Проверка, что элементы матрицы - Number
                    if not isinstance(elem, Number):
                        valid_flag = False
                        # print('НЕ Прошли проверку Number')
                        break
            else:
                valid_flag = False
                # print('НЕ Прошли проверку длины')
        else:
            valid_flag = False
            # print('НЕ Прошли проверку Iterable, int, int')
            
        return valid_flag
    
    
      
    def __add__(self, other: Self | Number) -> Self:
        return self.__element_wise_operation(op.add, other)
    
    def __radd__(self, other: Self | Number) -> Self:
        return self.__add__(other)
        
    def __sub__(self, other: Self | Number) -> Self:
        return self.__element_wise_operation(op.sub, other)
    
    def __rsub__(self, other: Self | Number) -> Self:
        result = self.__neg__()
        return result.__add__(other)
        
    def __mul__(self, other: Self | Number) -> Self:
        if isinstance(other, Matrix):
            raise NotImplementedError('умножение матриц будет реализовано в будущем')
        return self.__element_wise_operation(op.mul, other)
    
    def __rmul__(self, other: Self | Number) -> Self:
        return self.__mul__(other)
        
    def __neg__(self) -> Self:
        return self.__mul__(-1)
    
    @cache       
    def __repr__(self) -> str:
        output = ''
        
        max_elem_width = max(map(len, str(self.__flat).strip('()').split(', ')))
                
        for row in range(0, len(self.__flat), self.m):
            for ind in range(self.m):
                output += str(self.__flat[ind+row]).rjust(max_elem_width) + ' '
            output = output + '\n' 
        
        return output.rstrip('\n')
        
# Ручные тесты:
# >>> Matrix(1, 2, 3, 4, 5, n=2, m=3)
# ...
# ValueError: Невозможно сконструировать матрицу.
# >>>
# >>> from itertools import repeat
# >>>
# >>> m1 = Matrix(*repeat(1, 15), n=3, m=5)
# >>> m2 = Matrix(*range(1, 16), n=3, m=5)
# >>>
# >>> m1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# >>>
# >>> m2
# 1  2  3  4  5
# 6  7  8  9 10
# 11 12 13 14 15
# >>>
# >>> m1[0][0]
# ...
# TypeError: 'Matrix' object is not subscriptable
# >>>
# >>> m2.transpose
# 1  6 11
# 2  7 12
# 3  8 13
# 4  9 14
# 5 10 15
# >>>
# >>> m1 + m1
# 2 2 2 2 2
# 2 2 2 2 2
# 2 2 2 2 2
# >>>
# >>> m2 - m1
# 0  1  2  3  4
# 5  6  7  8  9
# 10 11 12 13 14
# >>>
# >>> m1 * m2
# ...
# NotImplementedError: умножение матриц будет реализовано в будущем
# >>>
# >>> 3 + m1
# 4 4 4 4 4
# 4 4 4 4 4
# 4 4 4 4 4
# >>>
# >>> m2.transpose - 10
# -9 -4  1
# -8 -3  2
# -7 -2  3
# -6 -1  4
# -5  0  5
# >>>
# >>> -1.5 - m1
# -2.5 -2.5 -2.5 -2.5 -2.5
# -2.5 -2.5 -2.5 -2.5 -2.5
# -2.5 -2.5 -2.5 -2.5 -2.5
# >>>
# >>> m3 + m1
# ...
# NameError: name 'm3' is not defined. Did you mean: 'm1'?
# >>> m3 = Matrix(*range(1, 5), n=2, m=2)
# >>> m3 + m1
# ...
# ValueError: Алгебраические операции возможны только с матрицами одной размерности.
# >>>
# >>> m3
# 1 2
# 3 4
# >>>
# >>> m3 * 4.5
# 4.5  9.0
# 13.5 18.0
# >>>
# >>> -m3
# -1 -2
# -3 -4
# >>>
# >>> m3 - [4,3,2,1]
# ...
# TypeError: Алгебраические операции возможны только с матрицами и числами.
