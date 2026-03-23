from collections import Counter

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count = 0
        freq = Counter(answers)  
        
        for x, num in freq.items():
            group_size = x + 1 
            groups = (num + group_size - 1) // group_size  
            count += groups * group_size  
        
        return count