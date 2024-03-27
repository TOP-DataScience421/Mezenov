InpNumStr = input('Введите трехзначное целое число: ')
InpNum = int(InpNumStr)
Hundreds = InpNum//100
Tens = (InpNum-(Hundreds*100))//10
Units = (InpNum-(Hundreds*100))%10

print('\nСумма цифр =', Hundreds+Tens+Units, '\nПроизведение цифр =', Hundreds*Tens*Units)

#Введите трехзначное целое число: 236

#Сумма цифр = 11
#Произведение цифр = 36