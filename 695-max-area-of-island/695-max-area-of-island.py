class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        visited = [[False for _ in range(m)] for _ in range(n)]
        max_ = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and not visited[i][j]:
                    max_ = max(max_, Solution.floodfill(grid,i,j,n,m,visited,0))
        return max_
    
    @staticmethod
    def floodfill(grid, r,c,n,m, visited, fill_count):
        def is_valid(r,c):
            return 0<=r<n and 0<=c<m and not visited[r][c] and grid[r][c] != 0
        options = [(0,1), (1,0), (-1,0) , (0,-1)]
        
        if is_valid(r,c):
            # fill
            fill_count+=1
            visited[r][c] = True
        else:
            return fill_count
        max_ = fill_count
        for option in options:
            max_ = max(max_, Solution.floodfill(grid, r+option[0],c+option[1],n,m,visited,max_))
        return max_