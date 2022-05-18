from bisect import bisect_right

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            current_item = numbers[i]
            rem_item = target-current_item
            rem_item_idx= bisect_right(numbers, rem_item, i)
            if numbers[rem_item_idx-1] == rem_item:
                return [i+1, rem_item_idx]
        
            
            
            
        