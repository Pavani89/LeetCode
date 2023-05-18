'''
1480. Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Time complexity: O(n)
Space complexity: O(n)
'''

def running_sum(nums):
    running_sum = []
    current_sum = 0
    for num in nums:
        current_sum += num
        running_sum.append(current_sum)
    return running_sum

'''
Optimised solution:
Time complexity: O(n)
Space complexity: O(1)
Do not use a output array but perform inplace update to input array

def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

'''
input = [1,2,3,5]
print(running_sum(input))

input2=[1,1,1,1,1]
print(running_sum(input2))