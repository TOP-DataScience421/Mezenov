scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

inp_word = input('Введите слово: ')
word_for_parse = inp_word.upper()
if 'Ё' in word_for_parse:
    word_for_parse = word_for_parse.replace('Ё', 'Е')
score = 0

#Итеррируемся по элементам словаря
for k,v in scores_letters.items():
    # print('Начало интерации по новому ключу: ')
    #Прерываем общий цикл прохода по словарю, если исследуемое слово "закончилось"
    if not word_for_parse:
        break
    
    #Итерируемся по буквам из поля v
    for letter in v:
        #Пока исследуемая буква присутствует в исследуемом слове, удаляем ее/увеличиваем счет на <кол-во букв>*<вес буквы(ключ словаря)>
        while letter in word_for_parse:
            # print(letter)
            #Увеличиваем счёт, учитывая кол-во букв в слове
            score += word_for_parse.count(letter)*k
            # print(score)
            #Удаляем букву(ы) из слова
            word_for_parse = word_for_parse.replace(letter, '')
            # print(word_for_parse)
            
print(f'\n{score=}')

# Пример вывода 1:
# Введите слово: синхрофазотрон

# score=29

# Пример вывода 2:
# Введите слово: водогрязеторфопарафинолечение

# score=58

