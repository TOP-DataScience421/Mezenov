from sys import path
from pathlib import Path
from pprint import pprint
from collections import deque
from utils import search_infile_for


def search_context(word_for_search: str, *another_words_for_search: str, context: int = 0) -> dict:
    """
    Функция принимает произвольный кортеж ключевых слов для поиска (но не меньше одного) совпадений в текстовых файлах в той же папке, откуда запущен скрипт. Также принимает необязательный параметр глубины контекста (кол-ва строк) вокруг найденного в файле ключевого слова
    Возвращает список словарей, в которых указаны такие параметры найденного в файле ключевого слова, как заданная глубина контекста, название файла, ключевое слово, строка на которой найдено слово, строка из текста в которой найдено слово с учетом глубины контекста
    """ 
 
    result_list = []
    
    path_for_search = Path(path[0]) / 'data'
    
    words_for_search = [word_for_search, *another_words_for_search]
    
    # Просматриваем папку с файлом скрипта
    for dir in path_for_search.walk():
        # Итерируемся по файлам в папке скрипта
        for file in dir[2]:
            # Проверяем расширение очередного файла, если 'txt' заходим внутрь
            if file.partition('.')[2] == 'txt':
                # Итерируемся по словам, которые нужно будет найти в файлах
                for word in words_for_search:
                    
                    # Чтобы запись не выглядела слишком громоздкой, выделил функционал с итерацией по конкретному файлу и непосредственному поиск в нем совпадений в отдельную функцию модуля utils
                    result = search_infile_for(path_for_search, file, word, context)
                    # Если возвращен не пустой список, добавляем его в общую переменную для вывода
                    if result:
                        result_list.append(result)
                    
        break
        
    return result_list
    
    
    
# Результат ручного теста:

    # >>> pprint(search_context('мысль', context = 1))
# [[{'context': 1,
   # 'filename': 'E3ln1.txt',
   # 'keyword': 'мысль',
   # 'line': 147,
   # 'text': ' - Сударыня! здесь, - сказал Чичиков, - здесь, вот где, - тут он '
           # 'положил руку на сердце, - да, здесь пребудет приятность времени, '
           # 'проведенного с вами! и поверьте, не было бы для меня большего '
           # 'блаженства, как жить с вами если не в одном доме, то, по крайней '
           # 'мере в самом ближайшем соседстве.\n'
           # '\n'
           # ' - А знаете, Павел Иванович, - сказал Манилов, которому очень '
           # 'понравилась такая мысль, - как было бы в самом деле хорошо, если '
           # 'бы жить этак вместе, под одною кровлею, или под тенью '
           # 'какого-нибудь вяза пофилософствовать о чем-нибудь, углубиться!..\n'
           # '\n'
           # ' - О! это была бы райская жизнь! - сказал Чичиков, вздохнувши. - '
           # 'Прощайте, сударыня! - продолжал он, подходя к ручке Маниловой. - '
           # 'Прощайте, почтеннейший друг! Не позабудьте просьбы!\n'},
  # {'context': 1,
   # 'filename': 'E3ln1.txt',
   # 'keyword': 'мысль',
   # 'line': 163,
   # 'text': 'Кучер, услышав, что нужно пропустить два поворота и поворотить на '
           # 'третий, сказал: «Потрафим, ваше благородие», - и Чичиков уехал, '
           # 'сопровождаемый долго поклонами и маханьями платка приподымавшихся '
           # 'на цыпочках хозяев.\n'
           # ' Манилов долго стоял на крыльце, провожая глазами удалявшуюся '
           # 'бричку, и когда она уже совершенно стала не видна, он все еще '
           # 'стоял, куря трубку. Наконец вошел он в комнату, сел на стуле и '
           # 'предался размышлению, душевно радуясь, что доставил гостю своему '
           # 'небольшое удовольствие. Потом мысли его перенеслись незаметно к '
           # 'другим предметам и наконец занеслись бог знает куда. Он думал о '
           # 'благополучии дружеской жизни, о том, как бы хорошо было жить с '
           # 'другом на берегу какой-нибудь реки, потом чрез эту реку начал '
           # 'строиться у него мост, потом огромнейший дом с таким высоким '
           # 'бельведером, что можно оттуда видеть даже Москву, и там пить '
           # 'вечером чай на открытом воздухе и рассуждать о каких-нибудь '
           # 'приятных предметах. Потом, что они вместе с Чичиковым приехали в '
           # 'какое-то общество в хороших каретах, где обворожают всех '
           # 'приятностию обращения, и что будто бы государь, узнавши о такой их '
           # 'дружбе, пожаловал их генералами, и далее, наконец, бог знает что '
           # 'такое, чего уже он и сам никак не мог разобрать. Странная просьба '
           # 'Чичикова прервала вдруг все его мечтания. Мысль о ней как-то '
           # 'особенно не варилась в его голове: как ни переворачивал он ее, но '
           # 'никак не мог изъяснить себе, и все время сидел он и курил трубку, '
           # 'что тянулось до самого ужина.'}],
 # [{'context': 1,
   # 'filename': 'r62Bf.txt',
   # 'keyword': 'мысль',
   # 'line': 19,
   # 'text': '«Понимаете ли, понимаете ли вы, милостивый государь, что значит, '
           # 'когда уже некуда больше идти? - вдруг припомнился ему вчерашний '
           # 'вопрос Мармеладова, - ибо надо, чтобы всякому человеку хоть '
           # 'куда-нибудь можно было пойти…»\n'
           # '\n'
           # 'Вдруг он вздрогнул: одна, тоже вчерашняя, мысль опять пронеслась в '
           # 'его голове. Но вздрогнул он не оттого, что пронеслась эта мысль. '
           # 'Он ведь знал, он предчувствовал, что она непременно «пронесется», '
           # 'и уже ждал ее; да и мысль эта была совсем не вчерашняя. Но разница '
           # 'была в том, что месяц назад, и даже вчера еще, она была только '
           # 'мечтой, а теперь… теперь явилась вдруг не мечтой, а в каком-то '
           # 'новом, грозном и совсем незнакомом ему виде, и он вдруг сам сознал '
           # 'это… Ему стукнуло в голову, и потемнело в глазах.\n'
           # '\n'
           # 'Он поспешно огляделся, он искал чего-то. Ему хотелось сесть, и он '
           # 'искал скамейку; проходил же он тогда по К-му бульвару. Скамейка '
           # 'виднелась впереди, шагах во ста. Он пошел сколько мог поскорее; но '
           # 'на пути случилось с ним одно маленькое приключение, которое на '
           # 'несколько минут привлекло к себе все его внимание.\n'},
  # {'context': 1,
   # 'filename': 'r62Bf.txt',
   # 'keyword': 'мысль',
   # 'line': 63,
   # 'text': ' - Бедная девочка! - сказал он, посмотрев в опустевший угол '
           # 'скамьи. - Очнется, поплачет, потом мать узнает… Сначала прибьет, а '
           # 'потом высечет, больно и с позором, пожалуй и сгонит… А не сгонит, '
           # 'так все-таки пронюхают Дарьи Францовны, и начнет шмыгать моя '
           # 'девочка, туда да сюда… Потом тотчас больница (и это всегда у тех, '
           # 'которые у матерей живут очень честных и тихонько от них '
           # 'пошаливают), ну а там… а там опять больница… вино… кабаки… и еще '
           # 'больница… года через два-три - калека, итого житья ее девятнадцать '
           # 'аль восемнадцать лет от роду всего-с… Разве я таких не видал? А '
           # 'как они делались? Да вот все так и делались… Тьфу! А пусть! Это, '
           # 'говорят, так и следует… Такой процент, говорят, должен уходить '
           # 'каждый год… куда-то… к черту, должно быть, чтоб остальных освежать '
           # 'и им не мешать. Процент! Славные, право, у них эти словечки: они '
           # 'такие успокоительные, научные. Сказано: процент, стало быть, и '
           # 'тревожиться нечего. Вот если бы другое слово, ну тогда… было бы, '
           # 'может быть, беспокойнее… А что, коль и Дунечка как-нибудь в '
           # 'процент попадет!.. Не в тот, так в другой?..\n'
           # '\n'
           # '«А куда ж я иду? - подумал он вдруг. - Странно. Ведь я зачем-то '
           # 'пошел. Как письмо прочел, так и пошел… На Васильевский остров, к '
           # 'Разумихину я пошел, вот куда, теперь… помню. Да зачем, однако же? '
           # 'И каким образом мысль идти к Разумихину залетела мне именно теперь '
           # 'в голову? Это замечательно».\n'
           # '\n'
           # 'Он дивился себе. Разумихин был один из его прежних товарищей по '
           # 'университету. Замечательно, что Раскольников, быв в университете, '
           # 'почти не имел товарищей, всех чуждался, ни к кому не ходил и у '
           # 'себя принимал тяжело. Впрочем, и от него скоро все отвернулись. Ни '
           # 'в общих сходках, ни в разговорах, ни в забавах, ни в чем он как-то '
           # 'не принимал участия. Занимался он усиленно, не жалея себя, и за '
           # 'это его уважали, но никто не любил. Был он очень беден и как-то '
           # 'надменно горд и несообщителен: как будто что-то таил про себя. '
           # 'Иным товарищам его казалось, что он смотрит на них на всех, как на '
           # 'детей, свысока, как будто он всех их опередил и развитием, и '
           # 'знанием, и убеждениями, и что на их убеждения и интересы он '
           # 'смотрит как на что-то низшее.\n'}]]
    
    

    
    