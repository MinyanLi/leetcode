# add up all the character correlated int
# find match of minus rule, then minus 2 fold because the previous addition

class Solution:
    def romanToInt(self, s: str) -> int:
        
        # dictionary of roman and int correlation
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        r = 0
        end = len(s) - 1
        
        for i, c in enumerate(s):      # enumerate returns count and value of iteration
            r += d[c]                  # d[c] is the cordinate int, this adds all the int
            
            if i < end:                # from 1st character to last but 2 character
                if c == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):    # if character in i position is "I" and character in (i+1) position is "V" or "X", r-=2, because previously already added 1, if want to be -1, need to -2
                    r -= 2
                if c == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):    # similar as above
                    r -= 20
                if c == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):    # similar as above
                    r -= 200
        
        return r
