def orth_triangle (*, cat1: float = None, cat2: float = None, hyp: float = None) -> float | None:
    
    #Проверка, что не был введен катет1
    if not cat1:
        #Проверка, что были введены катет2 и гипотенуза
        if cat2 and hyp:
            #Проверка, что гипотенуза больше введенного катета
            if hyp > cat2:
                #Расчет по теореме Пифагора
                return (hyp**2 - cat2**2) ** 0.5
    #Проверка, что не был введен катет2
    elif not cat2:
        #Проверка, что были введены катет1 и гипотенуза
        if cat1 and hyp:
            #Проверка, что гипотенуза больше введенного катета
            if hyp > cat1:
                #Расчет по теореме Пифагора
                return (hyp**2 - cat1**2) ** 0.5
    #Проверка, что не была введена гипотенуза
    elif not hyp:
        #Проверка, что были введены катеты
        if cat1 and cat2:
            #Расчет по теореме Пифагора
            return (cat1**2 + cat2**2) ** 0.5
    
    #Если добрались сюда, значит ввод был некорректный, возвращаем None
    return None
    
# Примеры ручных тестов:
# >>> print(orth_triangle(cat1 = 3))
# None
# >>> print(orth_triangle(cat1 = 3, cat2 = 2, hyp = 3))
# None
# >>> print(orth_triangle(cat1 = 3, hyp = 3))
# None
# >>> print(orth_triangle(cat1 = 3, hyp = 2))
# None
# >>> print(orth_triangle(cat1 = 3, hyp = 4))
# 2.6457513110645907
# >>> print(orth_triangle(cat1 = 3, hyp = 5))
# 4.0
# >>> print(orth_triangle(cat1 = 9, hyp = 3))
# None
# >>> print(orth_triangle(cat1 = 8, cat2 = 15))
# 17.0