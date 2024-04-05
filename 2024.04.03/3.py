EnteredYear = int(input('Введите год: '))

if (not EnteredYear % 4 and EnteredYear % 100 or not EnteredYear % 400):
    print('\nда')
else:
    print('\nнет')
    
#Пример вывода 1:
#Введите год: 2024

#да

#Пример вывода 2:
#Введите год: 2023

#нет