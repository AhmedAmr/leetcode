class UnionQuickFind():
    def __init__(self, n):
        self.n = n
        self.roots = list(range(self.n))
    
    def find(self, node: int) -> int:
        """
        Returns the root node index.
        Since we're using quick find method, we're maintaining that roots[node]'s parent will be always its root node.
        Runtime Complexity: O(1)
        Args:
            node (int): the node index to return its root node
        """
        return self.roots[node]

    
    def union(self, node1: int, node2: int) -> None:
        """Given 2 nodes' indices, join both of them into the same disjoin set.
        On worst case, we'd need to update most of entries in array, then it has linear time complexity.
        Runtime Complexity: O(N)

        Args:
            node1 (int): first node index
            node2 (int): second node index
        """
        root1 = self.find(node1)
        root2 = self.find(node2)

        # if both nodes have the same root, then they are in the same disjoint set, no action is needed
        if root1 != root2:
            for i, node in enumerate(self.roots):
                if node == root2:
                    self.roots[i] = root1

    def is_connected(self, node1: int, node2: int) -> bool:
        """Checks whether both node1 and node2 is connected together.
        This means in an undirected graph, there is at least one path sharing both node1 and node2

        Args:
            node1 (int): first node index
            node2 (int): second node index

        Returns:
            bool: true if both nodes are connected together, false otherwise
        """
        return self.find(node1) == self.find(node2)

    
    def size(self):
        return len(set(self.roots))
    

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionQuickFind(n)
        for s,e in edges:
            if uf.is_connected(s,e):
                return False
            uf.union(s,e)
        return uf.size() == 1
            