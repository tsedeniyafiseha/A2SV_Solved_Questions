import bisect

class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        res = 0
        
        for house in houses:
            i = bisect.bisect_left(heaters, house)
            
            left = float('inf')
            right= float('inf')
            
            if i > 0:
                left = house - heaters[i - 1]
            if i < len(heaters):
                right = heaters[i] - house
            
            res = max(res, min(left, right))
        
        return res