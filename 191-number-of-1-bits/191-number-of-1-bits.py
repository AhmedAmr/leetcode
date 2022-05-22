class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        cur = n
        while(cur != 0):
            cur&=(cur-1)
            c+=1
        return c