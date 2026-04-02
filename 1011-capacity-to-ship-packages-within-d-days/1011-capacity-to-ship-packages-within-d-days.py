class Solution:
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            if self.canShip(weights, days, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def canShip(self, weights, days, capacity):
        days_used = 1
        current = 0

        for w in weights:
            if current + w > capacity:
                days_used += 1
                current = 0
            current += w

        return days_used <= days