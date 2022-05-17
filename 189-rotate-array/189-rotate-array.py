class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        rotated_items = nums[-k::] if k >0 else []
        for i in range(k):
            nums.pop()
        
        nums[0:0] = rotated_items
        
        
        