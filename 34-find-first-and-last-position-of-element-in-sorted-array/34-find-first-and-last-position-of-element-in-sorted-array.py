class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bin_search(nums, target, left, right, direction='left'):
            if left > right:
                return -1
            while(left <= right):
                mid = left+(right-left)//2
                if nums[mid] == target:
                    ## return the min between this finding the most left element 
                    if direction == 'left':
                        value = bin_search(nums, target, left, mid-1, direction=direction)
                    else:
                    # direction is right
                        value = bin_search(nums, target, mid+1, right, direction=direction)
                    if value != -1:
                        return value
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        return [
            bin_search(nums, target, 0, len(nums)-1),
            bin_search(nums, target, 0, len(nums)-1, direction='right')
        ]
        
        
        
            
        
        
        
        