# Runtime 97 ms Beats 5.35%
# Memory 14 MB Beats 25.24% 

class Solution:
    def addBinary(self, a: str, b: str) -> str:
      
        # make str into int for calculation
        al =[]
        bl =[]
        for i in range(len(a)):
            ad = int(a[i])
            al.append(ad)
        for i in range(len(b)):
            bd = int(b[i])
            bl.append(bd)

        # to make sure the two number lists are the same length
        if len(al) > len(bl):
            dif = len(al) - len(bl)
            for i in range(dif):
                bl.insert(0, 0)
        if len(bl) > len(al):
            dif = len(bl) - len(al)
            for i in range(dif):
                al.insert(0, 0)

        # add up the two number lists
        add = []
        for i in range(len(al)):
            add.append(al[i] + bl[i])

        # the raw add up might contain "2" which need to move to another digit
        add_up = []
        i = 0
        numplus = 0
        while i < len(add):
            num = numplus + add[~i]
            if num >= 2:
                num = num - 2
                numplus = 1
                add_up.insert(0, num)
            else:
                numplus = 0
                add_up.insert(0, num)
            if i == len(add) - 1:
                add_up.insert(0, numplus)
            i += 1

        # turn the number list into str again
        f = []
        for k in range(len(add_up)):
            dig = str(add_up[k])
            f.append(dig)
        if f[0] == "0":
            f = f[1:]
        final = "".join(f)
        
        return final

