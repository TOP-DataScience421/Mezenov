telegramm = input('Введите текст Вашей телеграммы: ')
char_price = 0.3
telegramm_cost = 0.0
symblos_str = ' .,:;!@#$%^&*()_-></\'\"'

#Итерируемся по всем символам телеграммы, прибавляем счетчик на стоимость одного символа при каждой итерации, если не натыкаемся на знак препинания из множества выше
for char in telegramm:
    if char not in symblos_str:
        telegramm_cost += char_price

#Выводим в консоль в нужном формате
print(f'\n{int(telegramm_cost // 1.0)} руб. {int(round(telegramm_cost % 1, 2) * 100)} коп.')

# Введите текст Вашей телеграммы: Изучение python - сложное, но интересное занятие!

# 12 руб. 0 коп.