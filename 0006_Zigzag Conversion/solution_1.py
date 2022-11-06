# Runtime 8297 ms Beats 5.1%
# Memory 22 MB Beats 5.6%

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        s = list(s)

        
        collection = []
        for i in range(numRows):
            collection.append([])

        i = 0 # column
        j = 0 # row
        while s != []:
            if j % (numRows - 1) == 0 or (i + j) % (numRows - 1) == 0:
                collection[i].append(s[0])
                s.pop(0)
            else:
                collection[i].append(" ")
            i += 1
            if i == numRows:
                i = 0
                j += 1

        sum = []
        for k in range(numRows):
            sum = sum + collection[k]

        read = ""
        for k in sum:
            if k != " ":
                read += k

        return read
