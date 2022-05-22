return solns.append(chosen)
​
for i, num in enumerate(nums):
if not visited[i]:
# visit
visited[i] = True
# rec
solve(n,k-1, chosen + [num])
#backtrack
visited[i] = False
solve(n,n, [])
return solns
```
​
### Heap's Algorithm:
​
Heap’s algorithm is used to generate all permutations of n objects. The idea is to generate each permutation from the previous permutation by choosing a pair of elements to interchange, without disturbing the other n-2 elements.
Following is the illustration of generating all the permutations of n given numbers.
​
Example:
Input:    1 2 3
Output: 1 2 3
2 1 3
3 1 2
1 3 2
2 3 1
3 2 1
​
Algorithm:
- The algorithm generates (n-1)! permutations of the first n-1 elements, adjoining the last element to each of these. This will generate all of the permutations that end with the last element.
- If n is odd, swap the first and last element and if n is even, then swap the ith element (i is the counter starting from 0) and the last element and repeat the above algorithm till i is less than n.
- In each iteration, the algorithm will produce all the permutations that end with the current last element.
​
```
class Solution:
def permute(self, nums: List[int]) -> List[List[int]]:
soln = []
# applying heap's algorithm
def heap_permute(l, size):
if size == 1:
soln.append(l.copy())
for i in range(size):
heap_permute(l, size-1)