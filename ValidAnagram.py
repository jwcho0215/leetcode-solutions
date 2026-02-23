class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = s.lower()
        t = t.lower()

        if len(s) != len(t):
            return False
        
        if "".join(sorted(s)) != "".join(sorted(t)):
            return False
        
        return True
        