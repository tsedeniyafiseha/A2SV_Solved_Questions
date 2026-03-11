class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        s=0
        for i in logs:
            if i=="../":
               if s > 0:
                    s-=1
            elif i=="./":
                continue 
            else:
                s+=1
        return s
                

                 