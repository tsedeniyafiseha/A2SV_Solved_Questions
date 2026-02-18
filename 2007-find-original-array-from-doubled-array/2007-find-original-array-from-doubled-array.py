from collections import Counter

class Solution(object):
    def findOriginalArray(self, changed):
        n = len(changed)
        
        if n % 2 != 0:
            return []
        
        changed.sort()
        count = Counter(changed)
        original = []
        
        for num in changed:
            if count[num] == 0:
                continue
            
            if count[2 * num] == 0:
                return []
            
            original.append(num)
            count[num] -= 1
            count[2 * num] -= 1
        
        return original
