class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words= s.split(" ")

       

        if len(pattern) != len(words):
            return False 
        map1={}
        map2={}

        for c, i in zip(words, pattern):
            if c  in map1 and map1[c] != i :
                return False 
            elif i  in map2 and map2[i] !=c :
                return False 
            map1[c]= i 
            map2[i]=c 
        return True 
        