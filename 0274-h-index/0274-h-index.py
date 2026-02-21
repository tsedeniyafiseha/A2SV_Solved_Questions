class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        sorted_c = sorted(citations)
        
        for i in range(n):
            if sorted_c[i] >= n - i:
                return n - i
        
        return 0
