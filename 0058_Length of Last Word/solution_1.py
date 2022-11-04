# Runtime 56 ms Beats 48.31%
# Memory 14 MB Beats 39.27%

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.strip().split(" ")
        return len(a[-1])
