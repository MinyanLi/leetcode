# 12s

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        rev_a, rev_b = a[::-1], b[::-1]
        
        res = ""
        carry = 0
        for index in range(max_len):
            num_a = rev_a[index] if index < len(rev_a) else '0'
            num_b = rev_b[index] if index < len(rev_b) else '0' 
            
            total = int(num_a) + int(num_b) + carry
            
            res = str(total % 2) + res
            carry = total // 2
        
        if carry:
            res = "1" + res
        
        return res
