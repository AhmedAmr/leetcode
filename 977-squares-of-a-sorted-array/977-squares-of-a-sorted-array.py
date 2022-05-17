class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        abs_nums = list(map(abs, nums))
        left = 0
        right = n-1
        
        result = []
        
        while(left <= right):
            left_abs = abs_nums[left]
            right_abs = abs_nums[right]
            if left_abs > right_abs:
                result.append(left_abs**2)
                left+=1
            else:
                result.append(right_abs**2)
                right-=1
        result.reverse()
        return result
                
            
            