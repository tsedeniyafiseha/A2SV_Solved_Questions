class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder ={0:-1}
        prefix= 0
        n= len(nums)
        r=0
        for i in range(n):
            prefix += nums[i]
            r= prefix % k
            if r not in remainder:
                remainder[r] =i
            elif i- remainder[r] >1:
                return True 
        return False 

            