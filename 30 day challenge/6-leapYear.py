#_________________An extra day is added to the calendar every four years as feb.29th, and the day is called leap day. 3 conditions are used to identify 'em:
#_____-It must be divisible by 4 and leave no remainder.If the year is divisible by 100, it must also be divisible by 400.If a year meets these three conditions, then it is a leap year.
#______Given a year, determine wether it is leap or not.

year = int(input('Tell me a year: '))

def leap(year):
    if (year % 4) == 0 or (year % 100) != 0 and (year % 400) == 0: 
        print('')
        print(f'Year {year} is a leap year.')
    else:
        print('')
        print(f'Year {year} is NOT a leap year.')
        
leap(year)
    