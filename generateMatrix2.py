# %%

from typing import List
class Solution:
    def init(self,n):
        self.matrix = [[0]*n for i in range(n)]
        self.max = n*n
    def spiral(self, s, n, x, y): # starting number, size, coordinates
        if s > self.max:
            return
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        nX= x
        nY= y
        self.matrix[nX][nY] = s
        s += 1
        for i in range(4):
            if i < 3 :
                for _ in range(n-1):
                    nX = nX + dx[i]
                    nY = nY + dy[i]
                    self.matrix[nX][nY] = s
                    s += 1
            else:
                for _ in range(n-2):
                    nX = nX + dx[i]
                    nY = nY + dy[i]
                    self.matrix[nX][nY] = s
                    s += 1
        self.spiral(s,n-2,nX,nY+1) 

    def generateMatrix(self, n: int) -> List[List[int]]:
        self.init(n)
        self.spiral(1,n,0,0)
        return self.matrix

s = Solution()
s.generateMatrix(5)
# %%
