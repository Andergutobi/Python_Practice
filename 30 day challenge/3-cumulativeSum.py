#________Write a program that asks the user for a number (n) and prints the sum of the numbers 1 to n. If the user enter's 3, the output will be 6 since 1+2+3=6.

n = int(input('Enter a number please: '))

sum_num = 0
for i in range(1, n+1):
    sum_num += i
print(f'The sum of numbers 1 to {n} is {sum_num}')

    
    