"""
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5), then the array would become [3,4,5,1,2]. Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

Given an array of integers and a number, d, perform d left rotations on the array. Return the updated array

Sample Input: 4

[1,2,3,4,5]

Sample Output: [5,1,2,3,4]

Explanation:

When we perform d=4 left rotations, the array undergoes the following sequence of changes:

[1,2,3,4,5]=> [2,3,4,5,1] => [3,4,5,1,2] => [4,5,1,2,3] => [5,1,2,3,4]
"""
def rotLeft(a, d):
    return a[d:] + a[:d]

num = int(input())
arr = input().split(",")
result = rotLeft(arr,num)
for x in result :
    print(x, end = " ")
