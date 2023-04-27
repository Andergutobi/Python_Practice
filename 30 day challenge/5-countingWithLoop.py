#_________________Make a program that counts down from a number given by an user and another one that counts up, from different imputs.

numberUp = -(int(input('Give me one number: ')))
numberDown = int(input('Give me another number: '))

while numberUp <= 0:
    print('')
    print(numberUp)
    numberUp = numberUp + 1
    
while numberDown >= 0:
    print('')
    print(numberDown)
    numberDown = numberDown - 1    