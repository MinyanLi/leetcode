# Runtime 103 ms Beats 50.75%
# Memory 13.9 MB Beats 91.16%

# I guess it would be more difficult to write in other languages

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        if re.fullmatch(p, s):
            return True
        return False
        
