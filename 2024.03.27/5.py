IntPartNum = input('Введите целую часть "миль": ')
FractPartNum = input('Введите дробную (десятую) часть "миль": ')
KmToMilesRatio = 1.61

Miles = float(IntPartNum) + float(FractPartNum)/10
Kilometers = Miles*KmToMilesRatio

print(f'\n{Miles:.1f} миль = {Kilometers:.1f} км')

#Введите целую часть "миль": 32
#Введите дробную (десятую) часть "миль": 2

#32.2 миль = 51.8 км