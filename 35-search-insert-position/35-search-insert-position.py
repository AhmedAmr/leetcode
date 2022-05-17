class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while(left <= right):
            mid = (left+right)//2
            mid_item = nums[mid]
            if target == mid_item:
                return mid
            if target > mid_item:
                left = mid+1
            else:
                right = mid-1
        return left
                