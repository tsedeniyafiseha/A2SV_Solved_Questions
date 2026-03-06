class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSub= nums[0]
        total=0

        for n in nums:
            if total <0:
                total=0
            total+=n
            maxSub= max(maxSub,total)
        return maxSub

        