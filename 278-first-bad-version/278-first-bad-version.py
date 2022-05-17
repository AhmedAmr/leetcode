import typing
from bisect import bisect_left
class Solution:
    
    ## PYTHIONIC SOLUTION PART 1
    def __getitem__(self, index: int) -> bool:
        return isBadVersion(index)
    
    
    def firstBadVersion(self, n: int) -> int:
        ## FULL IMPL SOLUTION
        # left = 1
        # right = n
        # while (left<right):
        #     mid = (left+right)//2
        #     mid_is_bad = isBadVersion(mid)
        #     if mid_is_bad:
        #         right = mid
        #     else:
        #         left = mid+1
        # return left
        
        ## PYTHIONIC SOLUTION PART 2

        return bisect_left(self, True, 1, n)
        
                
            
        