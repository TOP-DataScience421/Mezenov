CurrKingPos = input('Введите текщее положение Короля: ')
NextKingPos = input('Введите следующее положение Короля: ')

# Если любой символ положения меняется больше чем на 1, 
# значит Король так сходить не сможет. 
# Так же Король обязан куда-нибудь сходить, а не остаться на месте.
if abs(ord(CurrKingPos[0])-ord(NextKingPos[0])) <= 1 and abs(int(CurrKingPos[1])-int(NextKingPos[1])) <= 1 and CurrKingPos != NextKingPos:
    print('\nда')
else:
    print('\nнет')