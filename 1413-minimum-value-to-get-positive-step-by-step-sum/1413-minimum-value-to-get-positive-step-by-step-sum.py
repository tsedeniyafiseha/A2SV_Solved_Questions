class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_sum = float('inf') 
        curr_sum = 0
        
        for num in nums:
            curr_sum += num
            min_sum = min(min_sum, curr_sum)
        
        
        return 1 if min_sum >= 0 else 1 - min_sum