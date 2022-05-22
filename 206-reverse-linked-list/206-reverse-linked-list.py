# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        left = head
        right = head.next
        first = True
        
        while right:
            tmp = right.next
            right.next = left
            if first:
                left.next=None
                first=False
            left = right
            right=tmp
        return left
            
            