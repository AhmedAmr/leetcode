class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while (left<right):
            mid = (left+right)//2
            mid_is_bad = isBadVersion(mid)
            if mid_is_bad:
                right = mid
            else:
                left = mid+1
        return left
                
            
        