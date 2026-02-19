from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        
        if set(c1.keys()) != set(c2.keys()):
            return False
        
       
        if sorted(c1.values()) != sorted(c2.values()):
            return False
        
        return True
