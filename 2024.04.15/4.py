PROMPT = 'Введите пару код: описание ошибки: '

inp_data = input(PROMPT).split()
inp_dict = dict()

while inp_data:
    inp_dict |= ([inp_data])
    inp_data = input(PROMPT).split()
    
error_description = input('Введите описание ошибки: ')

for k, v in inp_dict.items():
    if error_description == v:
        print(f'\n{k}')
        break
else:
    print('\n! value error !')
    
# Пример ввода:

# Введите пару код: описание ошибки: AI2F неисправность_входа_AI2
# Введите пару код: описание ошибки: AnF вращение_в_обратном_направлении
# Введите пару код: описание ошибки: bOF перегрузка_тормозного_сопротивления
# Введите пару код: описание ошибки: brF неисправность_тормоза
# Введите пару код: описание ошибки: bUF короткое_замыкание_тормозного_модуля
# Введите пару код: описание ошибки: CrF1 неисправность_работы_цепи_предварительного_заряда
# Введите пару код: описание ошибки: CrF2 неисправность_зарядного_теристора
# Введите пару код: описание ошибки:

# Пример вывода 1:

# Введите описание ошибки: неисправность_тормоза

# brF

# Пример вывода 2:

# Введите описание ошибки: Короткое_замыкание_по_выходу_силового_модуля

# ! value error !

