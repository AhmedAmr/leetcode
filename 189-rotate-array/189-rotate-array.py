class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        rotated_items = []
        for i in range(k):
            item = nums.pop()
            rotated_items.append(item)
        nums.reverse()
        nums.extend(rotated_items)
        nums.reverse()
        
        
        