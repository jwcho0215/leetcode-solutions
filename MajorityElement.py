def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number = math.floor(len(nums)/2)
        ls = {}
        for x in nums:
            ls[x] = ls.get(x,0) + 1
        
        for key,value in ls.items():
            if value > number:
                return key

        return 0