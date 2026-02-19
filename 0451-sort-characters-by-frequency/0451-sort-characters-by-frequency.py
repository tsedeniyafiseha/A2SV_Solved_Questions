from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        count = Counter(s)  
        
       
        chars = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        
       
        result = []
        for ch in chars:
            result.append(ch * count[ch])
        
        return "".join(result)
