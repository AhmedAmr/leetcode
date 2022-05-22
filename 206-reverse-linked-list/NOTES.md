left = right
right=tmp
return left
```
​
### Recursive Approach
​
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
if head is None or head.next is None:
return head
revlist = self.reverseList(head.next)
head.next.next = head
head.next = None
return revlist
```
​
#### General Notes:
1- Iterative approach did have less runtime and memory compared to recursive solution, (different constants), both have the same time/space complexity