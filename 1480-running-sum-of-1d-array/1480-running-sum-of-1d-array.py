class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_=0
        result=[]
        for num in nums:
            sum_+=num
            result.append(sum_)
        return result 
        