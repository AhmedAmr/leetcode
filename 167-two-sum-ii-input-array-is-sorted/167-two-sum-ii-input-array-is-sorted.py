from bisect import bisect_right

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        locations = {item:i for i, item in enumerate(numbers)}
        for i in range(n):
            rem_item  = target - numbers[i]
            if rem_item in locations:
                return [i+1, locations.get(rem_item) +1]
        
            
            
            
        