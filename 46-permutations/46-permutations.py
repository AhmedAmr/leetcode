class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        visited = [False for _ in range(n)]
        solns = []
        
        def solve(n, k, chosen):
            if k == 0:
                return solns.append(chosen)

            for i, num in enumerate(nums):
                if not visited[i]:
                    # visit
                    visited[i] = True
                    
                    # rec
                    solve(n,k-1, chosen + [num])
                    
                    #backtrack
                    visited[i] = False
        
        solve(n,n, [])
        
        return solns