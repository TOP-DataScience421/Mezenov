def countable_nouns(n: int, fit_nouns: tuple[str, str, str]) -> str:
    
    # Простые проверки на соответствие числовым рядам
    if n % 10 == 1 and n % 100 != 11:
        return(fit_nouns[0])
    elif n % 10 in range(2,5) and n %100 not in range(12,15):
        return(fit_nouns[1])
    else:
        return(fit_nouns[2])
    
#Пример ручных тестов
# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(0, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(11, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(1254, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(2021, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2022, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(2012, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(2025, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(13, ("год", "года", "лет"))
# 'лет'
