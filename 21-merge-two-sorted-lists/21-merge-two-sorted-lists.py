# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def solve(node1, node2):
            if not node1:
                return node2
            if not node2:
                return node1
            
            if node1.val <= node2.val:
                node1.next = solve(node1.next, node2)
                return node1

            node2.next = solve(node1, node2.next)
            return node2
        return solve(list1, list2)
            