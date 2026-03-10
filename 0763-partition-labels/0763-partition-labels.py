class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res=[]
        lastidx={}
        for i, c in enumerate(s):
            lastidx[c]=i
        size, end = 0,0
        for i, c in enumerate(s):
            size+=1
            if lastidx[c]> end:
                end = lastidx[c]
            if i==end:
                res.append(size)
                size=0
        return res
                
