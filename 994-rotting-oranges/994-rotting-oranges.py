from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        fresh = set()
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        
        
        mins = 0
        while(q and fresh):
            size = len(q)
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            for i in range(size):
                node = q.popleft()
                for direction in directions:
                    nr = node[0] + direction[0]
                    nc = node[1] + direction[1]
                    if nr < n and nc < m and nr >=0 and nc >=0 and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh.remove((nr,nc))
            mins+=1
        return mins if not fresh else -1
        
                
                
            
            