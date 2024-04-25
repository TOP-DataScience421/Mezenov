PROMPT = 'Введите числа: '

inp_list1 = [int(num) for num in input(PROMPT).split()]
inp_list2 = [int(num) for num in input(PROMPT).split()]

if inp_list1 or inp_list2:
    for i in range(0, len(inp_list1)):
        if inp_list1[i: i+len(inp_list2)] == inp_list2:
            print('\nда')
            break
            
    else:
        print('\nнет')
else:
    print('\nда')
    
# Пример вывода 1:

# Введите числа: 12 13 14 1 3 2
# Введите числа: 1 3 2
# да

# Пример вывода 2:

# Введите числа: 1 2 3
# Введите числа: 3 2 1
# нет

# Пример вывода 3:

# Введите числа: 1
# Введите числа: 1 2
# нет