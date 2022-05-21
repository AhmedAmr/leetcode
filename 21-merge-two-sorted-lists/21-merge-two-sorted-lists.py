# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        def extract_head(list_):
            cur = list_
            if cur.next is None:
                return (cur, None)
            next_ = cur.next
            cur.next = None
            return (cur, next_)
            
        head1 = list1
        head2 = list2
        current = None
        if head1.val <= head2.val:
            current,head1 = extract_head(head1)
        else:
            current, head2 = extract_head(head2)
        head = current
        while head1 and head2:
            if head1.val <= head2.val:
                current.next, head1 = extract_head(head1)
            else:
                current.next, head2 = extract_head(head2)
            current = current.next
        if head1:
            current.next = head1
        if head2:
            current.next = head2
        return head