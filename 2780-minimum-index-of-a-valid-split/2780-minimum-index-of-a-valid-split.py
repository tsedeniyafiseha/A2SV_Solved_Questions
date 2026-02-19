from collections import Counter

class Solution:
    def minimumIndex(self, nums):
        
        x, total = Counter(nums).most_common(1)[0]
        
        left_count = 0
        n = len(nums)
        
        for i, v in enumerate(nums):
            if v == x:
                left_count += 1
            
           
            if left_count * 2 > (i + 1) and (total - left_count) * 2 > (n - i - 1):
                return i
        
        return -1
