# Runtime 54 ms Beats 58.89%
# Memory 13.9 MB Beats 54.69%

class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        for i in range(len(num)):
            if num[i] == "6":
                num[i] = "9"
                break
        num = "".join(num)
        num = int(num)
        return num
