class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_=0
        for i in range(len(nums)):
            if i> max_:
                return False 
            max_=max(max_,i+nums[i])
        return True 