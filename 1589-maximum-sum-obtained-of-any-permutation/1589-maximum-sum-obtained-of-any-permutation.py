class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)

        diff = [0] * (n + 1)
        for l, r in requests:
            diff[l] += 1
            diff[r + 1] -= 1

        
        freq = [0] * n
        curr = 0
        for i in range(n):
            curr += diff[i]
            freq[i] = curr

       
        nums.sort()
        freq.sort()

        
        ans = 0
        for i in range(n):
            ans = (ans + nums[i] * freq[i]) % MOD

        return ans