class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        res = []
        for i in order :
            if i in count:
                res.append(i * count[i])
                del count[i] 
        for i in count:
            res.append(i* count[i])

        return "".join(res)
                
                 