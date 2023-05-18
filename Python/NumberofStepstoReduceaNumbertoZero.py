'''
1342. Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
'''

# Time complexity: O(n)
# Space complexity: O(1)

def numberOfSteps(num):
    counter = 0
    while num != 0:
        if num % 2 == 0:
            counter += 1
            num = num//2
        else:
            num -= 1
            counter += 1
    return counter

# Testing the function
input = 14
print(numberOfSteps(input))

input2=8
print(numberOfSteps(input2))

input3=123
print(numberOfSteps(input3))