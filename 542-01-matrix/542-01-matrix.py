import sys
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
       
        rows = len(mat)
        cols = len(mat[0])
        
        dest = [[sys.maxsize for _ in range(cols)] for _ in range(rows)] 
        q = deque()
        
        # put all zeros in queue, as they represents starting points for bfs
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dest[i][j] = 0
                    q.append((i,j))
                    
        directions = [(1,0), (-1,0), (0,1),(0,-1)]
        
        while(q):
            x,y = q.popleft()
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                
                if new_x >= 0 and new_y >= 0 and new_x < rows and new_y < cols:
                    if dest[x][y] +1 < dest[new_x][new_y]:
                        dest[new_x][new_y] = dest[x][y]+1
                        q.append((new_x,new_y))
        return dest
            