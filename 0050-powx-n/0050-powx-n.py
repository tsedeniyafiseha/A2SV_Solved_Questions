class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
      
        def power(x, n):
            if n == 0:
                return 1
            half = power(x, n // 2)
            return half * half if n % 2 == 0 else half * half * x

        return 1 / power(x, -n) if n < 0 else power(x, n)