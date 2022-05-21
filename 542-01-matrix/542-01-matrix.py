import sys
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        dest = [[sys.maxsize for _ in range(m)] for _ in range(n)]
        
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        def is_valid(r,c):
            return (0<=r<n and 0<=c<m and not visited[r][c])
            
            
        q= deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    dest[i][j] = 0
                    q.append((i,j,0))
        options = [(1,0), (-1,0), (0,1),(0,-1)]
        while(q):
            cr,cc,co = q.popleft()
            if is_valid(cr, cc):
                visited[cr][cc] = True
                dest[cr][cc] = min(dest[cr][cc], co)
                for option in options:
                    nr= cr+option[0]
                    nc = cc+option[1]
                    q.append((nr,nc, co+1))

        return dest
            
            