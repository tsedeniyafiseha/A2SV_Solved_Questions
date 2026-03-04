class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        diff = [0] * (n + 1)
        
        # Step 1: Record shifts
        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1
        
        # Step 2: Build prefix sum
        result = []
        current_shift = 0
        
        for i in range(n):
            current_shift += diff[i]
            
            # Convert character
            new_char = (ord(s[i]) - ord('a') + current_shift) % 26
            result.append(chr(new_char + ord('a')))
        
        return "".join(result)