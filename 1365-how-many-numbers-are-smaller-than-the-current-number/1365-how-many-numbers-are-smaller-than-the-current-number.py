class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s= sorted(nums)

    
        result={}
        for i, num in enumerate (s):
           if not num in result :
               result[num]=i
        return [result[num] for num in nums]
        
