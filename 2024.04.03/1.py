Sum=Num1=Num2=Num3=0

Num1 = float(input('Введите число 1: '))
Num2 = float(input('Введите число 2: '))
Num3 = float(input('Введите число 3: '))

if Num1 > 0:
    Sum += Num1
if Num2 > 0:
    Sum += Num2
if Num3 > 0:
    Sum += Num3
    
if Sum != 0:
    print(f'\nСумма введённых положительных чисел: ', Sum)
else:
    print('\nПоложительных чисел не было введено, увы...')


#Пример вывода 1:
#Введите число 1: 15.2
#Введите число 2: 4
#Введите число 3: -7

#Сумма введённых положительных чисел:  19.2

#Пример вывода 2:
#Введите число 1: -1
#Введите число 2: -15.6
#Введите число 3: -888

#Положительных чисел не было введено, увы...