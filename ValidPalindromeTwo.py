class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        for i in range(len(s)):
            if(s[i] != s[(len(s) - 1 ) - i]):
                original = s.copy()
                #left check
                s.pop(i)
                t = s.copy()
                s.reverse()
                if t == s:
                    print(t,s)
                    return True
                #right check
                original.pop((len(original) - 1 ) - i)
                real = original.copy()
                original.reverse()
                if real == original:
                    return True
                return False
        
        return True