# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def size(head: Optional[ListNode]):
            current = head
            ll_size = 0
            while(current):
                ll_size+=1
                current = current.next
            return ll_size

        def seek(head:Optional[ListNode], n: int) -> Optional[ListNode]:
            if n<0:
                return None
            current_idx = 0
            current = head
            while(current_idx!=n):
                current = current.next    
                current_idx+=1
            return current
        
        ll_size = size(head)
        if ll_size > 1:
            remove_index = ll_size - n
            if remove_index == 0:
                return head.next
            prev_ptr = seek(head, remove_index-1)
            next_ptr = prev_ptr.next
            if next_ptr:
                prev_ptr.next = next_ptr.next
            else:
                prev_ptr.next = None
        else:
            return None
        return head

            
        
        
        
        