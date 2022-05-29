class Solution:
    class UnionQuickFind():
        def __init__(self, n):
            self.n = n
            self.roots = list(range(self.n))

        def find(self, node: int) -> int:
            return self.roots[node]


        def union(self, node1: int, node2: int) -> None:
            root1 = self.find(node1)
            root2 = self.find(node2)

            if root1 != root2:
                for i, node in enumerate(self.roots):
                    if node == root2:
                        self.roots[i] = root1

        def is_connected(self, node1: int, node2: int) -> bool:
            return self.find(node1) == self.find(node2)

        
        def size(self):
            return len(set(self.roots))
            

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = Solution.UnionQuickFind(n)
        
        for i in range(n):
            for j in range(n):
                item = isConnected[i][j]
                if item:
                    uf.union(i,j)

        return uf.size()
        