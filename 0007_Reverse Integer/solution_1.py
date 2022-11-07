# Runtime 29 ms Beats 98.6%
# Memory 14 MB Beats 16.25%

class Solution:
    def reverse(self, x: int) -> int:
        s = list(str(x))
        r1 = []
        r2 = []
        r3 = []

        if s[0] == "-":
            r1.append("-")
            s.pop(0)

        for i in range(len(s)):
            r2.append(int(s[~i]))
            r3.append(s[~i])

        if len(r2) == 10:
            if r2[0] > 2:
                return 0
            if r2[0] == 2:
                if r2[1] > 1:
                    return 0
                if r2[1] == 1:
                    if r2[2] > 4:
                        return 0
                    if r2[2] == 4:
                        if r2[3] > 7:
                            return 0
                        if r2[3] == 7:
                            if r2[4] > 4:
                                return 0
                            if r2[4] == 4:
                                if r2[5] > 8:
                                    return 0
                                if r2[5] == 8:
                                    if r2[6] > 3:
                                        return 0
                                    if r2[6] == 3:
                                        if r2[7] > 6:
                                            return 0
                                        if r2[7] == 6:
                                            if r2[8] > 4:
                                                return 0
                                            if r2[8] == 4:
                                                if r2[9] > 7:
                                                    return 0

        r = r1 + r3
        r = "".join(r)
        r = int(r)
        return r
