class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        rotated_items = nums[-k::] if k >0 else []
        rotated_items.reverse()
        for i in range(k):
            nums.pop()
        nums.reverse()
        nums.extend(rotated_items)
        nums.reverse()
        
        
        