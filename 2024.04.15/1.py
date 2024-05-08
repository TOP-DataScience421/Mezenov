e_mail = input('Введите название Вашей электронной почты: ')

correct_email_flag = True

#Разделяем строку в кортеж на 3 элемента до '@', саму '@' и после '@'
separated_email = e_mail.partition('@')

#Если какая-либа строка в кортеже пустая, то адрес некорректный
if not separated_email[0] or not separated_email[1] or not separated_email[2]:
    correct_email_flag = False
#Если находим в первой половине адреса '.', то адрес некорректный
elif separated_email[0].find('.') >= 0:
    correct_email_flag = False
#Если не находим ни одной '.' во второй половине адреса, то адрес некорректный
elif separated_email[2].find('.') < 0:
    correct_email_flag = False
#Если находим еще '@' в какой-то части имени адреса, то адрес некорректный
elif separated_email[0].find('@') >= 0 or separated_email[2].find('@') >= 0:
    correct_email_flag = False
#Если в части с '.' отсутствуют какие-то элементы (пустые строки), то такой адрес некорректный
elif not separated_email[2].partition('.')[0] or not separated_email[2].partition('.')[1] or not separated_email[2].partition('.')[2]:
    correct_email_flag = False
#Если в адресе несколько '.' подряд (без символов между ними), то адрес некорректный
for e in range(len(separated_email[2])):
    if separated_email[2][e] == '.' and separated_email[2][e+1] == '.':
        correct_email_flag = False
        break
        
    
#Вывод решения о корректности адреса в консоль   
if correct_email_flag:
    print('\nда')
else:
    print('\nнет')
    
# Вариант вывода 1:

# Введите название Вашей электронной почты: 123@mail.ru

# да   

# Вариант вывода 2:

# Введите название Вашей электронной почты: 1@@mail.ru

# нет

# Вариант вывода 3:  
  
# Введите название Вашей электронной почты: 123@m.sdf.df.ru

# да

# Вариант вывода 4:

# Введите название Вашей электронной почты: 123@m.sdf..ru

# нет