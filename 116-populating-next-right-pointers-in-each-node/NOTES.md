### Recursive Solution
​
```python3
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
```
​
### Level Order Traversal
​
```python3
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
return roo
```
​