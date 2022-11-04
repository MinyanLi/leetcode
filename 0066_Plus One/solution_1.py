# Runtime 62 ms Beats 48.40%
# Memory 14 MB Beats 11.83%

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = []
        for i in range(len(digits)):
            a = str(digits[i])
            d.append(a)

        k = "".join(d)
        k = int(k)
        k = k + 1
        k = str(k)
        s = []
        for i in range(len(k)):
            s.append(k[i])
        return s
