from collections import deque
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
        if not root or root.left is None:
            return root
        q = deque([root.left, root.right, None])
        
        while(q != deque([None])):
            while(q):
                left_node = q.popleft()
                right_node = q.popleft()
                left_node.next = right_node
                if left_node.left:
                    q.append(left_node.left)
                if left_node.right:
                    q.append(left_node.right)
                if right_node is None:
                    break
                q.appendleft(right_node)
            q.append(None)
        return root
                
        