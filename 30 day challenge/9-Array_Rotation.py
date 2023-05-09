#

def rotLeft(a, d):
    return a[d:] + a[:d]

num = int(input())
arr = input().split(",")
result = rotLeft(arr,num)
for x in result :
    print(x, end = " ")
