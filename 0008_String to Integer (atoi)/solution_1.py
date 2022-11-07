# Runtime 86 ms Beats 6.70%
# Memory 13.9 MB  Beats 29.22%

class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        if s == "":
            return 0
            
        d = []
        
        neg = False
        if s[0] == "-":
            neg = True

        if s[0] == "-" or s[0] == "+" or s[0].isdigit():
            d.append(s[0])
        else:
            return 0

        for i in range(1, len(s)):
            if s[i].isdigit():
                d.append(s[i])
            else:
                break
        
        if d[0] == "+" or d[0] == "-":
            d.pop(0)

        if d == []:
            return 0

        for i in range(len(d)):
            if d[i].isdigit == False:
                return 0

        d = "".join(d)

        d = int(d)
        if neg == True:
            d = -d
        if d < - 2 ** 31:
            d = - 2 ** 31
        if d > 2 ** 31 -1:
            d = 2 ** 31 -1

        return d
Console
