### BFS on 1s
Correct solution but would result in TLE
​
```python3
import sys
from collections import deque
class Solution:
def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
n = len(mat)
m = len(mat[0])
visited = set()
def is_valid(r,c):
return (0<=r<n and 0<=c<m and (r,c) not in visited)
def bfs(r,c):
q= deque([(r,c,0)])
options = [(1,0), (-1,0), (0,1),(0,-1)]
while(q):
cr,cc,co = q.popleft()
if is_valid(cr, cc):
v = mat[cr][cc]
visited.add((cr,cc))
if v == 0:
return co
for option in options:
q.append((cr+option[0],cc+option[1], co+1))
for i in range(n):
for j in range(m):
visited = set()
if mat[i][j] == 1:
mat[i][j] = bfs(i,j)
return mat
```
​
### BFS on 0s [Accepted]