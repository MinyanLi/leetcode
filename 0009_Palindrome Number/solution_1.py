# Runtime 171 ms Beats 11.53%
# Memory 13.9 MB Beats 16.36%

class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math
        s = str(x)
        for i in range(math.ceil(len(s)/2)):
            if s[i] != s[~i]:
                return False
        return True
