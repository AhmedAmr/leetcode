from collections import Counter
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def drop_empty_values(map_: dict):
            return defaultdict(int, {k:v for k,v in map_.items() if v!=0})
    
        n = len(s1)
        m = len(s2)
        
        if n > m:
            return False
        
        s1map = dict(Counter(s1))
        s2map = defaultdict(int, dict(Counter(s2[0:n])))
        
        if s1map == s2map:
            return True
        s2map = drop_empty_values(s2map)
        
        for i in range(1, m-n+1):
            s2map[s2[i-1]]-=1
            s2map[s2[i+n-1]]+=1
            s2map = drop_empty_values(s2map)
            if s1map == s2map:
                return True
        return False
    
    
            