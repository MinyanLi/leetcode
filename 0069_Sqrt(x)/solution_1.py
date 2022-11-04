# Runtime 1935 ms  Memory 13.9 MB

class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        while True:
            if (n * n <= x):
                n = n + 1
            else:
                return n - 1
