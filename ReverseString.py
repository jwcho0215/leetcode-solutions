class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for x in range(len(s)):
            k = s.pop()
            s.insert(x,k)