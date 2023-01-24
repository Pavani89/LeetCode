class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            reminder = target - nums[i]
            if reminder in hashmap:
                return [i, hashmap[reminder]]
            hashmap[nums[i]] = i
        return None
