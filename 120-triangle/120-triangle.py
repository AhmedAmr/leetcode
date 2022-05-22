from copy import deepcopy
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = 1
        old = deepcopy(triangle)
        visited = [[False for _ in range(i)] for i in range(1,n+1)]
        for i in range(n):
            for j in range(m):
                head_value = triangle[i][j]
                if i+1 < n:
                    if visited[i+1][j]:
                        triangle[i+1][j]= min(triangle[i+1][j], old[i+1][j]+head_value)
                    else:
                        triangle[i+1][j] += head_value
                        visited[i+1][j] = True
                        
                    if visited[i+1][j+1]:
                        triangle[i+1][j+1]= min(triangle[i+1][j+1], old[i+1][j+1]+head_value)
                    else:
                        triangle[i+1][j+1]+=head_value
                        visited[i+1][j+1] = True
                        
            m+=1
        return min(triangle[-1])
                
                
                
                
            
            