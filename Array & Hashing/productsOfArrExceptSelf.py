# Time, Space - O(n), O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            answer = [1] * len(nums)
            prefix = 1
            postfix = 1

            for i in range(len(nums)):
                answer[i] = prefix
                prefix = prefix * nums[i]
            # answer = [1, 1, 2, 6]
                
            for i in range(len(nums) - 1, -1, -1):
                answer[i] *= postfix
                postfix = postfix * nums[i]
            # answer = [1*24, 1*12, 2*4, 6*1]
                
            return answer

# Input-   [1,   2,  3, 4]
# prefix-  [1,   1,  2, 6]
# postfix- [24, 24, 12, 4]
# output-  [24, 12,  8, 6]
