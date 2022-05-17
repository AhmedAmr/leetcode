class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        squared_nums = list(map(lambda v: v**2, nums))
        left = 0
        right = n-1
        result = []
        while(left <= right):
            left_sqr = squared_nums[left]
            right_sqr = squared_nums[right]
            if nums[left] > 0:
                result.extend(list(reversed(squared_nums[left:right+1])))
                break
            if left_sqr > right_sqr:
                result.append(left_sqr)
                left+=1
            else:
                result.append(right_sqr)
                right-=1
        result.reverse()
        return result