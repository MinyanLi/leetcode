# 15ms

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def fib(n):
            return fib(n-1) + fib(n-2) if n > 1 else n
        return fib(n+1)
