class Tetrahedron:
    """
    Класс Tetrahedron.
    Описывает правильный тетраэдр.
    
    Методы класса:
    __init__() 
    
    surface() -> float вычисляет площадь поверхности
    volume() -> float вычисляет объём тела
    """
    
    def __init__(self, edge: float):
        self.edge = edge
        
    def surface(self) -> float:
        """
        Метод класса.
        Возвращает площать поверхности правильного тетраэдра
        """
        
        return self.edge**2 * 3**0.5
        
    def volume(self) -> float:
        """
        Метод класса.
        Возвращает объем правильного тетраэдра
        """
        
        return (self.edge**3 / 12) * 2**0.5
        
        
# Результаты ручных тестов:
# >>> a = Tetrahedron(5)
# >>> a.surface()
# 43.30127018922193
# >>> a.volume()
# 14.73139127471974
# >>> a.edge = 12.5
# >>> a.surface()
# 270.6329386826371
# >>> a.volume()
# 230.17798866749595
        