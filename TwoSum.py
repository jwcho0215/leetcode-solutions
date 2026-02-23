def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            result = []
            for y in range(x + 1,len(nums)):
                if nums[x] + nums[y] == target:
                    result.append(x)
                    result.append(y)
                    return result
        return result