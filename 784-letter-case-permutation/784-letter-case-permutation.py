class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        m = 0
        for c in s:
            if c.isalpha():
                m+=1
        perm_count = 2**m
        permutations = []
        functions = [str.lower, str.upper]
        for i in range(perm_count):
            bin_val = bin(i)[2:].rjust(m,'0')
            max_bin = len(bin_val)
            chars = list(s)
            cur = 0
            for i,char in enumerate(chars):
                if cur >= max_bin:
                    break;
                if char.isalpha():
                    chars[i] = functions[int(bin_val[cur])](chars[i])
                    cur+=1
            
            permutations.append(''.join(chars))
        return permutations
                    
                    
                    
        