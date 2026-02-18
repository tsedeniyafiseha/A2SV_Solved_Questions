class Solution(object):
    def restoreString(self, s, indices):
        n = len(s)
        result = [""] * n
        
        for i in range(n):
            result[indices[i]] = s[i]
        
        return "".join(result)
