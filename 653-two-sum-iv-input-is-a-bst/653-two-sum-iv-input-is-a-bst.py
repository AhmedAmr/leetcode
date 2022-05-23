# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()

        def traverse(root):
            if root is None:
                return False
            return any([traverse(root.left),visit(root),traverse(root.right)])

        def visit(root):
            nonlocal k, visited
            val = root.val
            if val in visited:
                return True
            visited.add(k - val)
            return False
        

        return traverse(root)


