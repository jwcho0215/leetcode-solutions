class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False
        s = s.replace(" ","").lower()
        result = ""
        for c in s:
            if c.isalpha() or c.isnumeric():
                result += c
        if result == result[::-1]:
            return True
        return False

