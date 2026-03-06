class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        count= Counter({0:1})
        s=0
        diff=0
        ans =0

        for num in nums:
            s+=num
            diff= s-goal 
            ans+=count[diff]
            count[s]+=1
        return ans 
            
