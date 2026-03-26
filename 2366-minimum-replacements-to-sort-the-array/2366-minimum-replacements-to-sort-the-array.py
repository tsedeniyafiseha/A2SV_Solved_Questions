class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        prev=nums[-1]
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i]> prev:
                k=(nums[i]+prev-1)//prev
                count+=k-1
                prev=nums[i]//k
            else:
                prev=nums[i]
        return count


            