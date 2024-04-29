def strong_password(password: str) -> bool:
    # Объявление флагов и набора спец символов необходимых для работы
    spec_litterals = '!@#$%^&*_-<>'
    spec_flag = False
    lenght_flag = False
    nums_flag_prev = False
    nums_flag = False    
    upper_flag = False
    lower_flag = False
    
    # Проверка на длину пароля
    if len(password) > 7:
        lenght_flag = True
    
    # Итерируемся по символам пароля, чтобы исследовать символы на соответствие требованиям
    for lit in password:
        if not lower_flag and lit.islower():
            lower_flag = True
        if not upper_flag and lit.isupper():
            upper_flag = True
        if not spec_flag and not lit.strip(spec_litterals):
            spec_flag = True
        if not nums_flag and lit.isnumeric():
            if nums_flag_prev:
                nums_flag = True
            else:
                nums_flag_prev = True
    
# Если хоть один флаг не был поднят в True, значит пароль не соответствует требованиям    
    return spec_flag&lenght_flag&nums_flag&upper_flag&lower_flag

# Пример вывода 1:

# >>> strong_password('1abcD!7a')
# True    

# Пример вывода 2

# >>> strong_password('1abcD!')
# False

# Пример вывода 3:

# >>> strong_password('Password')
# False