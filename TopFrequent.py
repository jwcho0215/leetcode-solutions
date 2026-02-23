class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ls = defaultdict(list)
        for x in nums:
            ls[x].append(0)
        sorted_ls = sorted(ls.items(), key=lambda x:len(x[1]),reverse=True)
        result = []
        for x,y in sorted_ls[:k]:
            result.append(x)
        return result