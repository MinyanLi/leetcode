# 19ms

class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()  # remove space
        
        if not s:      # empty string
            return 0
          
        i = 0
        sign = 1    # positive or negative
        num = "0"
        
        # first character is +/-
        if s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i += 1
            
        # i = 1 if +/-
        while i < len(s):
            if not s[i].isdigit():
                break
            num += s[i]
            i += 1

        res = int(num) * sign
        
        return min(max(-2**31, res), 2**31 - 1)
