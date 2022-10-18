
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[]
        
        for i in range(numRows):
            triangle.append([])
            for j in range(i+1):
                if j==0 or i==j:
                    triangle[i].append(1)
                else:
                    triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
                    
        return triangle
