# Глобальные словарь соответствий символов -> числам в системах счислений разных базисов
literas_convertions = dict()
for k in range(0, 36):
    if k < 10:
        literas_convertions.setdefault(''.join(chr(ord('0') + k)), k)
    else:
        literas_convertions.setdefault(''.join(chr(ord('A') + k - 10)), k)

# Инверитрованный словарь соответствий, для удобства при обратных преобразованиях       
reversed_literas_convertions = dict()
for k, v in literas_convertions.items():
    reversed_literas_convertions.setdefault(v, k)
        
        
def int_base(num_to_conv: str, inp_base: int, out_base: int) -> str | None:
    """Преобразует число представленное одним базисом в другой. При ошибках возвращает None"""
    
    # Проверка оснований преобразования на вхождение в заданный диапазон
    if inp_base not in range(2, 36) or out_base not in range(2, 36):
        return None
    # Проверка, что в функцию были переданы адекватные параметры (не None, например)
    if not num_to_conv or not inp_base or not out_base:
        return None 
    
    return dec_to_out_base_convertor(inp_base_to_dec_convertor(num_to_conv, inp_base), out_base)
    
def inp_base_to_dec_convertor(num_to_conv: str, inp_base: int) -> int | None:
    """Преобразует переданное число из заданного для числа базиса в десятичное число. При ошибках возвращает None"""
    
    inp_num_to_dec = 0
    n = 0
    
    # Итерируемся по символам переданного числа (в виде строки) в обратном порядке
    for l in num_to_conv[::-1]:
        # Проверка на адекватность записи числа указанному базису
        if literas_convertions[l.upper()] < inp_base:
            # Непосредственное преобразование числа исходный базис -> десятичный базис
            inp_num_to_dec += literas_convertions[l.upper()]*inp_base**n 
        else:
            return None
        n += 1
        
    return inp_num_to_dec
    
def dec_to_out_base_convertor(dec_num: int | None, out_base) -> str | None:
    """Преобразует переданное десятичное число к переданному основанию, при ошибках возвращает None"""
    
    reminder = dec_num
    output_num = ''
    
    # Проверка, что в функцию не было передано None вместо десятичного числа
    if dec_num == None:
        return None
    elif dec_num == 0:
        return 0
  
    # Итерируемся по остатку от деления переданного числа на заданное основание
    while reminder:
        # Записываем новый символ из словаря преобразования при итерациях
        output_num += reversed_literas_convertions[reminder % out_base]
        # Уменьшаем остаток от деления методом взятия целого от деления предыдущего остатка на заданное основание
        reminder //= out_base
    else:
        # При использовании такого метода преобразования, получается посимвольно инвертированное число, разворачиваем его в "правильную сторону"
        output_num = ''.join(reversed(output_num))
    
    # Возвращаем полученное число, которое по факту является строкой смволов
    return output_num
        
    
    
# Ручные тесты функций
# >>> print(int_base('101010111100110121101111',2,16))
# None
# >>> print(int_base('101010111100110111101111',2,16))
# ABCDEF
# >>> print(int_base('ABCDEF',16,2))
# 101010111100110111101111
# >>> print(int_base('ABCDEF',16,35))
# 7HLBF
# >>> print(int_base('7hlbf',35,16))
# ABCDEF
# >>> print(int_base('00',35,16))
# 0
# >>> print(int_base('100',35,16))
# 4C9
# >>> print(int_base('1',35,16))
# 1
# >>> print(int_base('256',10,2))
# 100000000
# >>> print(int_base('256',0,2))
# None
# >>> print(int_base('256',1,2))
# None
# >>> print(int_base('256',36,2))
# None
# >>> print(int_base('256',10,0))
# None
# >>> print(int_base('256',10,36))
# None
# >>> print(int_base('25A',10,2))
# None
