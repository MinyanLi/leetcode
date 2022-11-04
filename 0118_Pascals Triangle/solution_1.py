# Runtime 38 ms Beats 83.91%
# Memory 13.8 MB Beats 97.25%


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if (numRows == 1):
            List = [[1]]
            return List
        elif (numRows == 2):
            List = [[1], [1, 1]]
            return List
        else:
            List = [[1], [1, 1]]
            for i in range(2, numRows):
                l = [1]
                for j in range(1, i):
                    l.append(List[i-1][j-1] + List[i-1][j])
                l.append(1)
                List.append(l)
            return List




