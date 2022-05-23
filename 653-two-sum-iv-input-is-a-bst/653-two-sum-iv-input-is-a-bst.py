# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        list_ = []
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            list_.append(root.val)
            traverse(root.right)
        
        traverse(root)
        i = 0
        j = len(list_)-1
        while(i<j):
            element_sum = list_[i]+list_[j]
            if element_sum == k:
                return True
            if element_sum < k:
                i+=1
            else:
                j-=1
        
        return False
