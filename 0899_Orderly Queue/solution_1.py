# Runtime 314 ms Beats 7.6%
# Memory  15.3 MB Beats 5.88%

# when K = 1, list all the possibilies and choose the smallest string
# when K >= 2, it is possible to sort all the items in a string, so just output the sorted string

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        s = list(s)

        collection = []
        temp = []
        if k == 1:
            for j in range(len(s)):
                for i in range(1, len(s)):
                    temp.append(s[i])
                temp.append(s[0])
                temp = "".join(temp)
                collection.append(temp)
                s = temp
                temp = []
            return min(collection)

        if k >= 2:
            s.sort()
            s = "".join(s)
            return s
                
