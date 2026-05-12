class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()

        def canPlace(distance):

            count = 1
            last = position[0]

            for i in range(1, len(position)):

                if position[i] - last >= distance:
                    count += 1
                    last = position[i]

            return count >= m

        left = 1
        right = position[-1] - position[0]

        answer = 1

        while left <= right:

            mid = (left + right) // 2

            if canPlace(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna