#______________Write a program that gets user's number grade and prints a letter grade.100 to 85 is A, 84 to 70 is B, 69 to 60 is C, 59 to 50 is D, and anything below 50 is F.

ng = float(input('Tell me your number grade, please: '))

def grade(ng):
    
    if ng<=100 and ng>=85:
        lt = 'A'
    elif ng<=84 and ng>70:
        lt = 'B'
    elif ng<=69 and ng>60:
        lt = 'C'
    elif ng<=59 and ng>50:
        lt = 'D'
    elif ng<=50:
        lt = 'F'    
    else:
        lt = 'Wrong number, Number-Grade has to be between 0 and 100. Try again.'               
    return lt;
if ng<=100 and ng>=0:
    print('')
    print(f'Your Letter Grade is {grade(ng)}')
else:
    print('')
    print(grade(ng))    