class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1  # Will hold the length of the longest increasing subsequence found.

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    # Update res since the longest subsequence might not start at nums[0].
                    res = max(res, dp[i])
        
        # Return res, not dp[0], because the longest increasing subsequence can end anywhere in the array.
        return res


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

'''
The overall solution to the problem—the length of the longest increasing subsequence in the 
entire array—doesn't necessarily end with the first element (nums[0]). It could end anywhere in the array. 
That's why you maintain a separate variable res to keep track of the longest length found so far while iterating through the array.

The reason you can't simply return dp[0] as the final solution is that the LIS might not start at nums[0]. 
It might start later in the array, or the longest sequence might be entirely contained within a later part of the array.
'''
