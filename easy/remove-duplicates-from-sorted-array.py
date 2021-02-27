# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur_index = 0
        for i in range(1,len(nums)):
            if nums[cur_index] != nums[i]:
                cur_index+=1
                nums[cur_index] = nums[i]
        return cur_index+1