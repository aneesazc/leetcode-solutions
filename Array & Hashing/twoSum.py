class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val: index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [i, prevMap[diff]]
            prevMap[num] = i

# Time- O(n)
# Space - O(n)
