class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i] <= 8:
                digits[i]+=1
                break
            digits[i] = 0
            
            if i == 0:
                digits.insert(0, 1)
                break
        return digits
        