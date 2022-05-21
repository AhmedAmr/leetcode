# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def merge(node1, node2):
            if node1 is None and node2 is None:
                return 
            if node1 is not None and node2 is not None:
                newNode = TreeNode(val=node1.val + node2.val)
                newNode.left = merge(node1.left, node2.left)
                newNode.right = merge(node1.right, node2.right)
            elif node1 is not None:
                newNode = TreeNode(val=node1.val)
                newNode.left = merge(node1.left, None)
                newNode.right = merge(node1.right, None)
            else:
                newNode = TreeNode(val=node2.val)
                newNode.left = merge(None, node2.left)
                newNode.right = merge(None, node2.right)
            return newNode
        
        return merge(root1, root2)
                
            