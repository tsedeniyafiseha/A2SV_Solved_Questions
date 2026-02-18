class Solution(object):
    def separateDigits(self, nums):
        result = []
        
        for num in nums:
            digits = []
            
            while num > 0:
                digits.append(num % 10)
                num //= 10
            
            # digits are reversed
            result.extend(digits[::-1])
        
        return result
