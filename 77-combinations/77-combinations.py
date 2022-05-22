class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        visited = [False for _ in range(n+1)]
        solns = []
        def solve(n, k, start_index, chosen):
            if k == 0:
                return solns.append(chosen)

            for i in range(start_index,n+1):
                if not visited[i]:
                    # visit
                    visited[i] = True
                    
                    # rec
                    solve(n,k-1,i, chosen + [i])
                    
                    #backtrack
                    visited[i] = False
            # return solns
        
        solve(n,k,1, [])
        
        return solns