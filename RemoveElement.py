def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        x = 0
        while x < len(nums):
            if nums[x] == val:
                nums.pop(x)
            else:
                x += 1 
                

        return len(nums)