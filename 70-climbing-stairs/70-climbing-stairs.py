from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache
        def count(n):
            if n==0:
                return 1
            if n<0:
                return 0
            return sum([count(n-1), count(n-2)])
        return count(n)