# 16ms

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = int(a, base=2)
        num_b = int(b, base=2)
        
        num_c = num_a + num_b
        
        return format(num_c, "b")
