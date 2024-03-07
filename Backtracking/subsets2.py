# Time: O(n * 2^n), Space: O(n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, curSet = [], []

        def backtrack(i):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return

            # decision to include nums[i]
            curSet.append(nums[i])
            backtrack(i + 1)

            # decision to NOT include nums[i]
            curSet.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return subsets
