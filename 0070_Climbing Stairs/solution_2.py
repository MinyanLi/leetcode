# Runtime 47 ms Beats 71.35%
# Memory 13.9 MB Beats 57.47%


class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        from functools import lru_cache   # need cache to shorten time

        @lru_cache
        def f(n):
            if n > 2:
                n = f(n-1) + f(n-2)
            return n

        n = f(n)
        return n
