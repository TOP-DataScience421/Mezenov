def central_tendency(num1: float, num2: float, /, *nums: float) -> dict[str, float]:
    
    investigated_nums = (num1, num2, *nums)
    output = {
                'median': 0.0,
                'arithmetic': 0.0,
                'geometric': 1.0,
                'harmonic': 0.0
             }
    
    #Выносим длину получившегося кортежа чисел в отдельную переменную для дальнейшего использования
    l_length = len(investigated_nums)
    
    #Вычисляем медианное значение исходя из кол-ва введенных чисел (четное/нечетное)
    if l_length % 2:
        output['median'] = investigated_nums[l_length//2]
    else:
        output['median'] = (investigated_nums[l_length//2] +
                            investigated_nums[l_length//2 - 1]) / 2
    
    #Один раз пробегаемся по всем введенным числам и делаем итеррируемые вычисления (сложения/умножения и т.д.)
    for n in range(0, l_length):
        output['arithmetic'] += investigated_nums[n]
        output['geometric'] *= investigated_nums[n]
        output['harmonic'] += 1/investigated_nums[n]
    #После завершения цикла, делаем разовые операции (деление на кол-во элементов, взятие корня и т.д.)
    else:
        output['arithmetic'] /= l_length
        output['geometric'] = output['geometric'] ** (1 / l_length)
        output['harmonic'] = l_length / output['harmonic']
    
    #Выводим получившийся словарь
    return output
    
# Пример ручных проверок:
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}
# >>> central_tendency(1, 2, 3)
# {'median': 2, 'arithmetic': 2.0, 'geometric': 1.8171205928321397, 'harmonic': 1.6363636363636365}
# >>> central_tendency(1, 2, 3, 4, 5)
# {'median': 3, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
# >>> central_tendency(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# {'median': 5.5, 'arithmetic': 5.5, 'geometric': 4.528728688116765, 'harmonic': 3.414171521474055}
# >>> central_tendency(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
# {'median': 8, 'arithmetic': 8.0, 'geometric': 6.423424749779761, 'harmonic': 4.520483676867457}
# >>> central_tendency(1, 2, 3, 4, 5, 50, 51, 53, 54, 55, 101, 102, 103, 104)
# {'median': 52.0, 'arithmetic': 49.142857142857146, 'geometric': 21.7539932599541, 'harmonic': 5.791014357388033}
# >>> central_tendency(1, 2, 3, 4, 5, 50, 51, 53, 54, 55, 101, 102, 103, 104, 105)
# {'median': 53, 'arithmetic': 52.86666666666667, 'geometric': 24.16104292585543, 'harmonic': 6.1803111173282845}