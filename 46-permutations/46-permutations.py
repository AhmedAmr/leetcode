class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        soln = []
        
        
        def heap_permute(l, size):
            if size == 1:
                soln.append(l.copy())
            
            for i in range(size):
                heap_permute(l, size-1)
                
                if size%2==0:
                    # even, swap ith with last
                    l[i],l[size-1] = l[size-1],l[i]
                else:
                    # odd, swap first with last
                    l[0], l[size-1] = l[size-1],l[0]
        heap_permute(nums, len(nums))           
        return soln
            
        