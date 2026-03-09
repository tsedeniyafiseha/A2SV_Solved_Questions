class Solution(object):
    def subarraysDivByK(self, nums, k):

        count = {0:1}
        prefix_sum = 0
        ans = 0

        for num in nums:

            prefix_sum += num

            remainder = prefix_sum % k

            if remainder < 0:
                remainder += k

            ans += count.get(remainder,0)

            count[remainder] = count.get(remainder,0) + 1

        return ans