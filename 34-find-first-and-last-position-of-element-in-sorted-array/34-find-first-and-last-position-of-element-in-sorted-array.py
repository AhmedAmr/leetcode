import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        n = len(nums)
        start = bisect.bisect_left(nums, target)
        end =  bisect.bisect_right(nums, target) - 1
        if start >= n or nums[start] != target:
            start = -1
        if end >= n or nums[end] != target:
            end = -1
        return [start,end]
            
        
        
        
        