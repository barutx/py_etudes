
# class Solution(object):
#     def maximumOddBinaryNumber(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
        
#         a = s.count("1")
#         b = s.count("0")
#         c = ""

#         for i in range(a-1):
#             c += "1"
#         for j in range(b):
#             c += "0"
#         c += "1"
#         return c
    


# k = Solution()
# print(k.maximumOddBinaryNumber("010"))

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        
        # nums_sqrt =sorted(list(map(lambda x : x**2, nums)), reverse=True)
        return sorted([i*i for i in nums])

sqrt = Solution()

nums = [1,2,6,7,12,43,21]
print(sqrt.sortedSquares(nums))


