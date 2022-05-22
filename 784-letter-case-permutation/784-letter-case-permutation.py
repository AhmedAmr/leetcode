class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        n = len(s)
        visited = [False for i in range(n)]
        permutations = []
        
        
        
        def permute(i, n):
            nonlocal s
            if i == n:
                permutations.append(s)
                return
            
            if s[i].isnumeric():
                return permute(i+1,n)
            
            options = [str.upper, str.lower]
            for func in options:
                if not visited[i]:
                    # visit
                    visited[i] = True
                    
                    new_char = func(s[i])
                    s = s[:i] + new_char + s[i+1:]
                    permute(i+1,n)
                    
                    #backtrack
                    visited[i] = False
        
        permute(0,n)
        return permutations
                    
        