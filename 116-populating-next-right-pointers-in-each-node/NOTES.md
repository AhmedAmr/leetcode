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
def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
if right_node is None:
break
q.appendleft(right_node)
q.append(None)
return roo
```
​
### Level Order Traversal (More concise solution)
```
class Solution:
def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
if not root or root.left is None:
return root
q = deque([root.left, root.right])
while(q):
size = len(q)
for i in range(size):
node = q.popleft()
if i < size-1:
node.next = q[0]
if node.left:
q.append(node.left)
if node.right:
q.append(node.right)
return root
```