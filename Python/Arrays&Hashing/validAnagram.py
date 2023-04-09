# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Optimised
        # Time: O(n)
        # Space:  O(n)

        # Iterate through string 1, maintain a hashmap of charaters with count
        # In another iteration thorugh string 2, decrement the count of charaters
        # At the end check the counter, if zero -> True else False
        s = s.replace(" ", "").lower()
        t = t.replace(" ", "").lower()

        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for char in t:
            if char in count:
                count[char] -= 1
            else:
                count[char] = 1
        
        for k in count:
            if count[k] != 0:
                return False

        return True
