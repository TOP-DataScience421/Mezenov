InpNumStr = input('Введите трехзначное целое число: ')
InpNum = int(InpNumStr)
Hundreds = InpNum//100
Tens = (InpNum-(Hundreds*100))//10
Units = (InpNum-(Hundreds*100))%10

print('Сумма цифр =',Hundreds+Tens+Units,'\nПроизведение цифр =',Hundreds*Tens*Units)