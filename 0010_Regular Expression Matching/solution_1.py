# Runtime 103 ms Beats 50.75%
# Memory 13.9 MB Beats 91.16%

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        if re.fullmatch(p, s):
            return True
        return False
        
