def repeat(func_obj: 'function', repeat_times: int = 2) -> 'function':
    """Функция-декоратор. Выполняет переданную в качестве аргумента функцию <repeat_times> раз"""
    
    def wrapper(*args, **kwargs) -> 'any':
        # Вызываем целевую функцию с произвольным кол-вом аргументов <repeat_times> раз
        for _ in range(0, repeat_times):
            func_obj(*args, **kwargs)
    return wrapper

# Примеры ручных тестов:
# >>> def test_func():
# ...     print('Питон!')
# ...
# >>> def squared_x(x: float | int) -> float:
# ...     print(x*x)
# ...
# >>> test_func = repeat(test_func, 4)
# >>> squared_x = repeat(squared_x, 6)
# >>> test_func()
# Питон!
# Питон!
# Питон!
# Питон!
# >>> squared_x(4)
# 16
# 16
# 16
# 16
# 16
# 16