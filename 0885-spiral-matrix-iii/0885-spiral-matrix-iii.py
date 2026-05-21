class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        
        result = []

        directions = [
            (0, 1),    # right
            (1, 0),    # down
            (0, -1),   # left
            (-1, 0)    # up
        ]

        result.append([rStart, cStart])

        steps = 1
        d = 0

        while len(result) < rows * cols:

            # repeat twice
            for _ in range(2):

                dr, dc = directions[d]

                for _ in range(steps):

                    rStart += dr
                    cStart += dc

                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        result.append([rStart, cStart])

                d = (d + 1) % 4

            steps += 1

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna