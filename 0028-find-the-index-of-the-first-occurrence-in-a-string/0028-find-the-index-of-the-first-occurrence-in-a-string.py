class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
          return 0
        n= len(needle)
        for l in range(len(haystack)-n+1):
            if haystack[l:l+n]==needle :  
               return l
        return -1
            