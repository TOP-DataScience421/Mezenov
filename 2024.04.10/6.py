ticket_number = list(input('Введите номер вашего билетика: '))
mid_of_ticket_numbers = len(ticket_number)/2
first_half=second_half=0

#Итерируемся по всем числам введённого билетика
for i in range(0, len(ticket_number)):
    #Сначала складываем числа первой половины билетика, потом второй
    if i < mid_of_ticket_numbers:
        first_half += int(ticket_number[i])
    else:
        second_half += int(ticket_number[i])

#Если сумма чисел первой половины равна сумме чисел второй половины выводим "да" в консоль, иначе "нет"      
if first_half == second_half:
    print('\nда')
else:
    print('\nнет')
    
# Пример вывода 1:

# Введите номер вашего билетика: 224620

# да

# Пример вывода 2:

# Введите номер вашего билетика: 123456

# нет