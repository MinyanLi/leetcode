# similar as solution_1
# if smaller character on left, minus
# if smaller character on right, plus


class Solution:
    def romanToInt(self, s: str) -> int:
        
        # dictionary of correlation
        roman={
                "I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000
        }
        
        res=0
        for i in range(len(s)):
            if i+1<len(s) and roman[s[i]] < roman[s[i+1]]:
                res-=roman[s[i]]
            else:
                res+=roman[s[i]]
        return res
                
