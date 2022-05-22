class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        
        cur = n
        while cur > 1:
            if cur%2 != 0:
                return False
            cur>>=1
        return True
        