Dividend = int(input('Ввведите целое число (делимое): '))
Divider = int(input ('Введите целое число (делитель): '))
IntegerOfDiv = Dividend//Divider
RemainderOfDiv = Dividend%Divider


if RemainderOfDiv:
    print(f'\n{Dividend} не делится на {Divider} нацело')
    print(f'неполное частное: {IntegerOfDiv}')
    print(f'остаток: {RemainderOfDiv}')
else:
    print(f'\n{Dividend} делится на {Divider} нацело')
    print(f'частное: {IntegerOfDiv}')
    
#Пример вывода 1:
#Ввведите целое число - делимое: 18
#Введите целое число - делитель: 7

#18 не делится на 7 нацело
#неполное частное: 2
#остаток: 4

#Пример вывода 2:
#Ввведите целое число - делимое: 10
#Введите целое число - делитель: 5

#10 делится на 5 нацело
#частное: 2