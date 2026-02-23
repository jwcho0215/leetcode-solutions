class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ls = dict()
        for x,y in enumerate(nums):
            if y in ls and abs(ls[y] - x) <= k:
                return True
            ls[y] = x
        return False