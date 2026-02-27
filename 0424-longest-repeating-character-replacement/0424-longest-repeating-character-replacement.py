class Solution(object):
    def characterReplacement(self, s, k):
        from collections import defaultdict
        
        count = defaultdict(int)
        longest=0
        l=0
        max_=0
        for r in range (len(s)):
            count[s[r]]+=1
            max_= max(max_,count[s[r]])
            while (r-l+1) - max_ >k:
                count[s[l]]-=1
                l+=1
            longest= max(longest,r-l+1)
        return longest 