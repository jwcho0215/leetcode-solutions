class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 1 not in nums:
            return 1
        if len(nums) == 1:
            return nums[0] + 1
        
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        result = 1
        for x in range(0,len(nums)):
            if nums[x] < 1:
                continue
            if x + 1 > len(nums) - 1:
                return nums[len(nums)-1] + 1
            else: 
                if nums[x] != nums[x + 1] - 1:
                    return nums[x] + 1
                else: 
                    result = nums[x] + 1
        
        
        return result 
        