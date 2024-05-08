def numbers_strip(num_list: list, n: int = 1, * , copy_sw: bool = False) -> list:
    
    #Отделяем варианты возврата самого объекта, либо его копии
    if copy_sw:
        #Написана отдельная функция по итерации
        return numbers_strip_iterrator(num_list.copy(), n)
    else:
        return numbers_strip_iterrator(num_list, n)  
            
    

#Функция итерации по обрезаемому списку
def numbers_strip_iterrator(num_list: list, n: int) -> list:
    
    n_counter = 0

    # Итерируемся пока не достигнем кол-ва требуемых обрезок n (итераций)
    while n_counter < n:
            #Если не проверить, что список еще есть, воткнемся в исключение. Если список уже опустел, ничего страшного, возвращаем пустой
            try:
                num_list.remove(max(num_list))
                num_list.remove(min(num_list))
            except ValueError:
                break
            n_counter += 1
        
    return num_list

# Пример ручного тестирования:    
# >>> num_list = [1,1,2,2,3,3,4,4,5,5]
# >>> new_list= numbers_strip(num_list, 2)
# >>> new_list
# [2, 2, 3, 3, 4, 4]
# >>> num_list
# [2, 2, 3, 3, 4, 4]
# >>> num_list is new_list
# True
# >>> num_list = [1,1,2,2,3,3,4,4,5,5]
# >>> new_list = numbers_strip(num_list, 2, copy_sw = True)
# >>> num_list
# [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
# >>> new_list
# [2, 2, 3, 3, 4, 4]
# >>> num_list is new_list
# False

    
