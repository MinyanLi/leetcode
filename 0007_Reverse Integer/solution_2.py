# 12ms
# but the probelem said "Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."
# how can you directly compare the interger with 2**31

class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x <0:
            neg=True
            x = x * -1
            
        rev =0
        while x:
            n = x %10
            x = x // 10
            rev = rev * 10 + n
            
        if neg:
            rev = rev* -1
            
        mi = 2 ** 31 * (-1)
        ma = 2 ** 31 - 1
        if rev < mi or rev > ma:
            return 0
        return rev
