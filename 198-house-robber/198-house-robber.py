import sys
from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache(maxsize=n+1)
        def solve(i):
            if i >= n:
                return 0
            
            # rob i
            option1 = nums[i] + solve(i+2)
            # don't rob i
            option2 = solve(i+1)
            
            return max(option1, option2)
            
        return solve(0)
            