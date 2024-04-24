# Написать программу, которая подсчитывает стоимость отправки телеграммы.

# В прошлом веке для отправки коротких текстовых сообщений люди использовали телеграммы. В разное время их стоимость рассчитывалась по-разному. Но при передаче телеграмм по ключу (морзянкой) стоимость отправки телеграммы зависит от количества знаков. 
# В нашей задаче примем, что один символ буквы или цифры стоит тридцать копеек.

# Программа получает из stdin строку с текстом телеграммы.
# Программа выводит в stdout стоимость в рублях и копейках, согласно формату в примере ниже.

telegramm = input('Введите текст Вашей телеграммы: ')
char_price = 0.3
telegramm_cost = 0.0

#Итерируемся по всем символам телеграммы, прибавляем счетчик на стоимость одного символа при каждой итерации
for char in telegramm:
    telegramm_cost += char_price

#Выводим в консоль в нужном формате
print(f'\n{int(telegramm_cost // 1.0)} руб. {int(round(telegramm_cost % 1, 2) * 100)} коп.')

# Введите текст Вашей телеграммы: Изучение python - сложное, но интересное занятие!

# 14 руб. 70 коп.