# Time: O(n * 2^n), Space: O(n)
# nums and subsets with no dubplicates
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums, subsets, curSet):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return

            # decision to include nums[i]
            curSet.append(nums[i])
            helper(i + 1, nums, subsets, curSet)
            curSet.pop()

            # decision NOT to include nums[i]
            helper(i + 1, nums, subsets, curSet)

        subsets, curSet = [], []
        helper(0, nums, subsets, curSet)
        return subsets
