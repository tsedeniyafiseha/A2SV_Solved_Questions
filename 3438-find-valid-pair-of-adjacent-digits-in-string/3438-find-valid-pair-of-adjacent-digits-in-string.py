from collections import Counter

class Solution(object):
    def findValidPair(self, s):
        s_count = Counter(s)
        
        for i in range(len(s) - 1):
            x = s[i]
            y = s[i + 1]
            
            if x != y and s_count[x] == int(x) and s_count[y] == int(y):
                return x + y
        
        return ""
