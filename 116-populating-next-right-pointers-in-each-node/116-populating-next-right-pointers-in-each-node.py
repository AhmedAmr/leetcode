"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def link(left_subtree, right_subtree):
            if left_subtree is None and right_subtree is None:
                return
            left_subtree.next = right_subtree
            link(left_subtree.left, left_subtree.right)
            link(right_subtree.left, right_subtree.right)
            link(left_subtree.right, right_subtree.left)
        
        link(root.left if root else None, root.right if root else None)
        return root