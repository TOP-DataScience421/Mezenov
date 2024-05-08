n = int(input('Введите кол-во чисел Фибоначчи для вывода в консоль: '))
i = 2
numbers_list = [1, 1]

#Итерируемся по циклу пока счетчик меньше введенного кол-ва чисел Фибоначчи для вывода
while i < n:
    #Каждый следующий элемент - сумма двух предыдущих
    numbers_list += [numbers_list[i-2] + numbers_list[i-1]]
    i += 1

#Выводим список разверткой со срезом, т.к. пользователь может захотеть вывести меньше 2х изначальных элементов списка    
print('\n', *numbers_list[:n])

# Пример вывода 1:

# Введите кол-во чисел Фибоначчи для вывода в консоль: 1

# 1

# Пример вывода 2:

# Введите кол-во чисел Фибоначчи для вывода в консоль: 25

 # 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025
