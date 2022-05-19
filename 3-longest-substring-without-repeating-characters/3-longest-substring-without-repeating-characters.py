from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        
        if n <= 1:
            return n
        
        h = defaultdict(lambda:-1)
        max_count = current_count = first = 0
        for last, char in enumerate(s):
            if  char not in h or h[char] < first:
                h[char] = last
                current_count+=1
            else:
                max_count = max([max_count, current_count])
                first = h[char] + 1
                h[char] = last
                current_count = last-first+1
        
        max_count = max([max_count, current_count])
        return max_count
        
        