import datetime as dt
import numbers
import decimal

class PowerMeter:
    """
    Класс PowerMeter
        Описывает двухтарифный счётчик потреблённой электрической мощности.
    
    Аттрибуты класса:
        tariff1: decimal.Decimal - первый тариф
        tariff2: decimal.Decimal - второй тариф
        tariff2_starts: datetime.time - время начала действия второго тарифа
        tariff2_ends: datetime.time - время окончания действия второго тарифа
        power: decimal.Decimal - суммарная потреблённая мощность
        charges: dict[datetime.date, decimal.Decimal] - начисления за каждый месяц согласно тарифным планам
    
    Методы класса:
        __init__()
        __repr__()
        __str__()
        
        meter(consumed_power: float) -> decimal.Decimal
            принимает значение потреблённой мощности, вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент
    """
    
    def __init__(self,
                tariff1: numbers.Number = 6.5,
                tariff2: numbers.Number = 5.0,
                tariff2_starts: dt.time = dt.time(22, 0, 0),
                tariff2_ends: dt.time = dt.time(6, 0, 0)
                ):
        
        self.tariff1 = decimal.Decimal(tariff1)        
        self.tariff2 = decimal.Decimal(tariff2) 
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        # decimal.Decimal - суммарная потреблённая мощность
        self.power = decimal.Decimal(0)
        # dict[datetime.date, decimal.Decimal] - начисления за каждый месяц согласно тарифным планам
        self.charges = {}
        self.charges[str(dt.date(dt.datetime.now().year, dt.datetime.now().month,day = 1))] = 0   
        
    def __repr__(self):
        return f'<{__class__.__name__}: {self.power:.2f} кВт/ч>'
        
    def __str__(self):
        # Вычисляем ключ словаря для текущего месяца
        cur_month_key = dt.date(dt.datetime.now().year, dt.datetime.now().month,day = 1)
        # Если такой ключ есть, возвращаем значение по ключу
        if str(cur_month_key) in self.charges.keys():
            return f'({cur_month_key:%b}) {self.charges[str(cur_month_key)]:.2f}'
        # Если такого ключа нет, возвращаем None
        return None
        
    def meter(self, consumed_power: float) -> decimal.Decimal:
        """
        Метод класса
        принимает значение потреблённой мощности, вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент
        """
        
        # Вычисляем ключ для словаря хранения сумм к оплате за месяц
        cur_month_key = dt.date(dt.datetime.now().year, dt.datetime.now().month,day = 1)
        # Вычисляем текущее время
        cur_time = dt.time(dt.datetime.now().hour, dt.datetime.now().minute, dt.datetime.now().second)
        
        # Прибавляем переданную энергию к накопленной
        self.power += decimal.Decimal(consumed_power)
        
        # Вычисляем какой тариф действует на данный момент
        tariff = self.tariff1
        if cur_time > self.tariff2_starts or dt.time(22, 0, 0) < cur_time < self.tariff2_ends:
            tariff = self.tariff2
        
        # Если по текущему месяцу уже были записи, то добавляем сумму с учетом текущего тарифа, если нет, то создаем новый ключ словаря для текущего месяца
        if str(cur_month_key) in self.charges.keys():
            self.charges[str(cur_month_key)] += decimal.Decimal(consumed_power) * tariff
        else:
            self.charges[str(cur_month_key)] = decimal.Decimal(consumed_power) * tariff
        
        # Возвращаем сумму за текущий месяц
        return self.charges[str(cur_month_key)].quantize(decimal.Decimal('1.00'))
            
        
# Ручные тесты:
 # 23:56:25 > python -i 2.py
# >>> pm1 = PowerMeter()
# >>> pm1.meter(4.3)
# Decimal('21.50')
# >>> pm1.meter(5)
# Decimal('46.50')
# >>> pm1.meter(2)
# Decimal('56.50')
# >>> pm1.meter(4.32)
# Decimal('78.10')
# >>> pm1
# <PowerMeter: 15.62 кВт/ч>
# >>> print(pm1)
# (May) 78.10    