from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        n= len(nums)
        response =[]
        counted_elt=Counter(nums)
        for i in counted_elt:
            if counted_elt[i] > n/3:
                response.append(i )
        return response 
















