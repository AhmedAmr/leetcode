from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        
        if n > m:
            return False
        
        s1map = dict(Counter(s1))
        
        for i in range(m-n+1):
            s2map = dict(Counter(s2[i:i+n]))
            if s1map == s2map:
                return True
        return False
            
            