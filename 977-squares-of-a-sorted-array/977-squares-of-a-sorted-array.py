class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def square(v):
            return int(math.pow(v,2))
        n = len(nums)
        negative_list = []
        positive_list = []
        for num in nums:
            if num < 0:
                negative_list.append(num)
            else:
                positive_list.append(num)
        
        negative_list = list(map(square, negative_list))
        positive_list = list(map(square, positive_list))
        positive_list.reverse()
        
        result = []
        for i in range(n):
            if not negative_list:
                result.extend(list(reversed(positive_list)))
                break
            if not positive_list:
                result.extend(list(reversed(negative_list)))
                break
            neg_item = negative_list[-1]
            pos_item = positive_list[-1]
            if neg_item <= pos_item:
                result.append(negative_list.pop())
            else:
                result.append(positive_list.pop())
        return result