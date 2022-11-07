# 16ms

# abs()


class Solution:
    def reverse(self, x: int) -> int:
        z= int(str(abs(x))[::-1])
        if x > 2147483647 or x < -2147483648 or z > 2147483647 or z < -2147483648 :
            return 0
        else:
            return -z if x<0 else z
