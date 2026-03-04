class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix={0:1}
        total= 0
        n= len(nums)
        res=0
        for i in range(n):
            total+=nums[i]
            diff = total- k
            
            res+= prefix.get(diff,0)
            prefix[total] = 1+ prefix.get(total,0)
        return res 
            