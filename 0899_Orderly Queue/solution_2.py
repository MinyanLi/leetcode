# 35ms


# Runtime 85 ms Beats 7.6%
# Memory 13.8 MB Beats 71.76%

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # abcd i: :i
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return ''.join(sorted(s))
