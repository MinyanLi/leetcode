class Solution:
    def modifyString(self, s: str) -> str:
      
        s = list(s) # use list will be more easy for mutate
        
        for i in range(len(s)):
            if s[i] == "?": 
                for c in "abc": 
                # because just need to avoid same letter immediately near by
                # there's maximum 2 letter to be eliminated
                # so "abc" should be enough for choose
                    if (i == 0 or s[i-1] != c) and (i+1 == len(s) or s[i+1] != c): 
                    # s[i] = "?"
                    # i == 0 means s[0] = "?"
                    # s[i-1] != c means the left side of s[i] is not a or b or c (at least one of them will be correct)
                    # i+1 == len(s) means s[-1] =="?"
                    # s[i+1] != c means the right side of s[i] is not a or b or c
                        s[i] = c
                        break 
        return "".join(s)
