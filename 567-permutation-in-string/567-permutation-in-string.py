from collections import Counter
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def drop_empty_values(map_: dict):
            return defaultdict(int, {k:v for k,v in map_.items() if v!=0})
    
        n = len(s1)
        m = len(s2)
        
        unique = len(set(s1))
        
        if n > m:
            return False
        
        s1map = dict(Counter(s1))
        s2map = None
        
        for i in range(0, m-n+1):
            if i == 0:
                s2map = defaultdict(int, dict(Counter(s2[i:n])))
            else:
                s2map[s2[i-1]]-=1
                s2map[s2[i+n-1]]+=1
                s2map = drop_empty_values(s2map)
            if len(s2map) == unique:
                if s1map == s2map:
                    return True
        return False
    
    
            