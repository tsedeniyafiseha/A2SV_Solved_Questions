from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        
        return result
