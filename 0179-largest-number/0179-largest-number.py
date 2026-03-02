class Solution(object):
    def largestNumber(self, nums):
        from functools import cmp_to_key
        
        str_nums = [str(num) for num in nums]
        
        
        def compare(n1, n2):
            
            if n1 + n2 > n2 + n1:
                return -1 
            elif n1 + n2 < n2 + n1:
                return 1 
            else:
                return 0  

        str_nums.sort(key=cmp_to_key(compare))
        
        
        if str_nums[0] == "0":
            return "0"
            
       
        return "".join(str_nums)