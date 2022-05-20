class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        def area(r,c):
            if not (0<= r < n and 0<= c < m and (r,c) not in visited and grid[r][c]):
                return 0
            
            visited.add((r,c))
            
            return (1 + area(r+1, c) +  area(r-1,c) + area(r, c+1) + area(r, c-1))
        return max(area(r,c) for r in range(n) for c in range(m))