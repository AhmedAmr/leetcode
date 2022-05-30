from collections import defaultdict, deque
class QuickUnionFindByRank():
    def __init__(self, n: int):
        self.n = n
        self.roots = list(range(self.n))
        self.ranks = [0] * self.n
    
    def find(self, node: int) -> int:
        if self.roots[node] == node:
            return node
        root = self.find(self.roots[node])
        self.roots[node] = root
        return root

    
    def union(self, node1: int, node2: int) -> None:
        root1 = self.find(node1)
        root2 = self.find(node2)
        rank1 = self.ranks[root1]
        rank2 = self.ranks[root2]

        if rank1 > rank2:
            self.roots[root2] = root1
        elif rank1 < rank2:
            self.roots[root1] = root2
        else:
            self.roots[root2] = root1
            self.ranks[root1] += 1


        def is_connected(self, node1: int, node2: int) -> bool:
            return self.find(node1) == self.find(node2)

        def size(self):
            return len(set(self.roots))
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = QuickUnionFindByRank(n)
        modified_indxes = set()
        for x,y in pairs:
            uf.union(x,y)
            if x!=y: 
                modified_indxes.add(x)
                modified_indxes.add(y)
        modified_indxes = sorted(list(modified_indxes))
        group_chars = defaultdict(list)
        for i in modified_indxes:
            group_idx = uf.find(i)
            group_chars[group_idx].append(s[i])
        group_chars = {k:v for k,v in group_chars.items() if len(v)!=1}
        s = list(s)
        for k in group_chars.keys():
            group_chars[k].sort()
            group_chars[k] = deque(group_chars[k])
        
        for i in modified_indxes:
            group_idx = uf.find(i)
            s[i] = group_chars[group_idx].popleft()
        return ''.join(s)
                
            
            
        
            
            
        