def taxi_cost(dist: int, wait_time: int = 0) -> int | None:
    
    #Объявляем разные константы для работы функции
    dist_cost = 6 / 150
    wait_time_cost = 3.0
    base_travel_cost = 80
    pending_cost = 80
     
    #Если один из передаваемых функции параметров был передан отрицательным, завершаем выполнение, возвращаем None
    if dist < 0 or wait_time < 0:
        return None
    
    #Расчитываем стоимость исходя из переданных параметров
    return round(base_travel_cost + dist * dist_cost + wait_time * wait_time_cost + (0 if dist else pending_cost))    
 
# Примеры вывода:
 
# >>> print(taxi_cost(-300))
# None
# >>> taxi_cost(42130,8)
# 1789
# >>> taxi_cost(0,5)
# 175
# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(825)
# 113
# >>> taxi_cost(825, 25)
# 188
# >>>