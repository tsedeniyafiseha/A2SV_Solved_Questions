class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff= [0]*52
        for start , end in ranges:
            diff[start]+=1
            diff[end+1]-=1
        coverage=0
        for i in range(1,52):
            coverage+= diff[i]
            if left<= i<= right and coverage==0:
                return False 
        return True 


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna