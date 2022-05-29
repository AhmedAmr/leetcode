class Solution:
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
            

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = Solution.QuickUnionFindByRank(n)
        
        for i in range(n):
            for j in range(n):
                item = isConnected[i][j]
                if item:
                    uf.union(i,j)
        for i in range(n):
            uf.find(i)

        return uf.size()
        