# O(n)/O(1) : Time/Memory
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMin * n
            curMin = min(n * curMin, n * curMax, n)  
            curMax = max(tmp, n * curMax, n)  # [-1, 8] -> -8 without considering n but we want max in this case to be 8 so we also consider n
            res = max(res, curMax)

        return res



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize the result with the maximum value in nums to handle cases where all numbers are negative.
        res = max(nums)
        # Initialize current minimum and maximum to 1. These variables track
        # the min and max product of the subarray ending at the current position.
        curMin, curMax = 1, 1

        for n in nums:
            # If the current number is 0, reset curMin and curMax since any product with 0 is 0.
            # This effectively starts calculating a new subarray product from the next number.
            if n == 0:
                curMin, curMax = 1, 1
                continue
            # Temporary copy of curMin is needed because curMin might change before calculating curMax.
            tmp = curMin * n
            # The new curMin is the minimum of the current number, its product with the previous curMin,
            # and its product with the previous curMax. This accounts for the effect of negative numbers.
            curMin = min(n * curMin, n * curMax, n)
            # The new curMax is the maximum of the same three possibilities.
            # We consider the temporary minimum (tmp) before its update,
            # ensuring we don't lose the value when n is negative and could potentially make a larger product.
            curMax = max(tmp, n * curMax, n)
            # Update the result if the current maximum product of a subarray ending here is greater than the current result.
            res = max(res, curMax)

        return res
