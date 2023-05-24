class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # optimum solution with hashSet
        # Time: O(n)
        # Space: O(n)

        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
