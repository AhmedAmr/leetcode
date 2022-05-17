import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while(left <= right):
            mid_idx = (left+right)//2
            mid_item = nums[mid_idx]
            if target == mid_item:
                return mid_idx
            if target > mid_item:
                left = mid_idx+1
            else:
                right = mid_idx-1
        return -1
                