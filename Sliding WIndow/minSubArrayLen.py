class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        L = 0
        curSum = 0

        for R in range(len(nums)):
            curSum += nums[R]
            # While current sum is greater than or equal to target, try to shrink the window from the left
            while curSum >= target:
                # Calculate the length of the current valid window
                res = min(res, R - L + 1)
                # Subtract the left-most value and move L to the right to see if we can find a smaller window
                curSum -= nums[L]
                L += 1

        return res if res != float('inf') else 0
