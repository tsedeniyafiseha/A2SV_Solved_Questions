class Solution(object):
    def countGoodNumbers(self, n):
        MOD = 10**9 + 7
        
        even_count = (n + 1) // 2
        odd_count = n // 2
        
        def power(base, exp):
            result = 1
            base %= MOD
            
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            
            return result
        
        return (power(5, even_count) * power(4, odd_count)) % MOD