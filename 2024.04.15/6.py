bin_num_pref = {'b', '0b'}
bin_nums = {'0', '1'}

inp_bin_num = input('Введите двоичное число: ')
#Сохраняем изначальную строку, чтобы потом проверить, что она была не пустая
parsed_bin_num = inp_bin_num

#Удаляем стандартные префиксы из введенного двоичного числа используя предопределенное множество префиксов
for l in bin_num_pref:
    parsed_bin_num = parsed_bin_num.strip(l)

#Удаляем все цифры '0' и '1' из оставшейся строки
for n in bin_nums:
    parsed_bin_num = parsed_bin_num.replace(n, '')

#Если в строке все еще есть символы или введенная изначально строка была пустая, значит введённое число не двоичное
if parsed_bin_num or not inp_bin_num:
    print('\nнет')
else:
    print('\nда')
    

# Пример вывода 1
# Введите двоичное число: 0b010101010

# да

# Пример вывода 2
# Введите двоичного число: b01010101

# да

# Пример вывода 3
# Введите двоичного число: 010101010

# да

# Пример вывода 4
# Введите двоичного число: 1b01010

# нет