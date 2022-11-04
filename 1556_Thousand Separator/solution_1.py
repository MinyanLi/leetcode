# 64 ms	13.9 MB

class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = list(str(n))
        m = len(n) % 3
        p = len(n) // 3

        if m == 0:
            for i in range(p-1):
                n.insert(3 + 4*(i),".")

        else:
            for i in range(0,p):
                n.insert(m+(4*i),".")
                
        return "".join(n)
