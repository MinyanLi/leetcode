# https://www.youtube.com/watch?v=Y0lT9Fck7qI

# Runtime 53 ms Beats 56.58%
# Memory 13.8 MB Beats 96.15%

class Solution:
    def climbStairs(self, n: int) -> int:
        
        one = 1
        two = 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one

