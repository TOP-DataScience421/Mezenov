digits = int(input('Введите количество разрядов: '))
max_num = int('9' * digits)
min_num = int('9' * (digits - 1)) + 1
simple_nums_counter = num = 0

print(f'{min_num = }  |  {max_num = }')

#Итерируемся по каждому числу от минимального до максимального для заданного кол-ва разрядов
for num in range(min_num, max_num):
    i = 0

    #Итерируемся до текущего числа (счетчика внешнего цикла)
    while i < num:
        i += 1
        #Если счетчик влож цикла делится на счетчик внешнего цикла нацело И они не равняются друг другу И счетчик влож цикла не равен 1 ИЛИ счетчик внешнего цикла равен 1 (так как 1 математически не является ПРОСТЫМ) то прерываем вложенный цикл, т.к. исследуемое число НЕ ПРОСТОЕ. Если проходим весь вложенный цикл до числа внешнего цикла, то число ПРОСТОЕ - увеличиваем счетчик.
        if not(num % i) and num != i and i != 1 or num == 1:
            break
        elif num == i:
            # print(num)
            simple_nums_counter += 1
            break
        
print(f'\nКоличество простых чисел до числа {max_num}: {simple_nums_counter}')

# Пример вывода:
# Введите количество разрядов: 5
# min_num = 10000  |  max_num = 99999

# Количество простых чисел до числа 99999: 8363