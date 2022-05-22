class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cur = nums[0]
        
        for idx in range(1,len(nums)):
            cur^=nums[idx]
        return cur
        
        