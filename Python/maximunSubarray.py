# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0

        for num in nums:
            # discard older sum if less than zero
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSub = max(maxSub, currSum)
        return maxSub
