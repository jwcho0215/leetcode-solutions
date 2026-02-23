def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        
        result = ""
        if len(strs) == 1:
            return strs[0]

        for x in range(len(strs[0])):
            toCheck = strs[0][x]
            for y in range(1,len(strs)):
                if x > len(strs[y]) - 1 or toCheck != strs[y][x]:
                    return result
                if toCheck == strs[y][x]:
                    if len(strs) - 1 == y:
                        result += toCheck
                        
                            
        return result
        