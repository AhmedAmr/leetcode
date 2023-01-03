class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        res = 0
        for target_index in range(n):
            last = -1
            for i in range(m):
                if last > ord(strs[i][target_index]):
                    res+=1
                    break
                else:
                    last = ord(strs[i][target_index])
        return res

