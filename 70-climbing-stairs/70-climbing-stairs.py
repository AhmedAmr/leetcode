class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [-1 for _ in range(n+1)]
        
        def count(n):
            if n==0:
                return 1
            if n<0:
                return 0
            if mem[n] != -1:
                return mem[n]
            mem[n] = sum([count(n-1), count(n-2)])
            return mem[n]
        return count(n)