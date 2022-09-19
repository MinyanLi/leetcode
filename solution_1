class Solution:
    def romanToInt(self, s: str) -> int:
        
        import sys

        # length constrain
        if len(s) > 15:
            sys.exit("too long string")
        if len(s) < 1:
            sys.exit("too short string")

        # value constrain
        l = "MDCLXVI"
        c = 0
        for i in s:
            for j in l:
                if i == j:
                    c = c + 1
        if c != len(s):
            sys.exit("not valid Roman string")

        # relate roman character and number
        num = [1000, 500, 100, 50, 10, 5, 1]
        d = dict(zip(l, num))

        # translate single characters in s to numbers
        s1 = []
        for i in s:
            s1.append(d[i])

        # compare number and posision
        # small number on left means minus
        # small number on right means plus
        n = 0
        if len(s) == 1:
            n = n + s1[0]
        elif len(s) > 1:
            for i in range(len(s)-1):
                if s1[i] < s1[i+1]:
                    n = n - s1[i]
                elif s1[i] >= s1[i+1]:
                    n = n + s1[i]
            n = n + s1[-1]

        return n
        
