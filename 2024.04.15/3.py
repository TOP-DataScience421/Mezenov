PROMPT = 'Введите числа: '

inp_list1 = [int(num) for num in input(PROMPT).split()]
inp_list2 = [int(num) for num in input(PROMPT).split()]
h_len = max(len(inp_list1), len(inp_list2))
l1_l2_choose = True if len(inp_list1) > len(inp_list2) else False

if inp_list1 or inp_list2:
    for i in range(0, h_len):
        if l1_l2_choose:
            if inp_list1[i: i+len(inp_list2)] == inp_list2:
                print('\nда')
                break
        else:
            if inp_list2[i: i+len(inp_list1)] == inp_list1:
                print('\nда')
                break
            
    else:
        print('\nнет')
else:
    print('\nда')
    
# Пример вывода 1:

# Введите числа: 1 2 3
# Введите числа: 3 2 1

# нет

# Пример вывода 2:

# Введите числа: 1 2 3
# Введите числа: 1 1 1

# нет

# Пример вывода 3:

# Введите числа: 1 2 3 4
# Введите числа: 1 2

# да

# Пример вывода 4:

# Введите числа: 1 2
# Введите числа: 1 2 3 4

# да