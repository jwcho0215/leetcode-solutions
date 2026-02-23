class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls = defaultdict(list)

        for w in strs: 
            word = "".join(sorted(w))
            ls[word].append(w)
        
        return list(ls.values())