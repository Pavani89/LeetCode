class Solution:

	# Use a delimiter with number and a charater
	# The number would represent the charater in the work that follows
	# charater to be used as a unique delimiter
	# Time: O(n)
	# Space: O(1)
	
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
		for s in strs:
			res += str(len(s)) + "#" + self
		return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [] , 0
		
		while i < len(str):
			j = i
			while j != "#":
				j += 1
			length = int(s[i:j])
			res.append(s[j + 1 : j + 1 + length])
			i = j + 1 + length
		return res
