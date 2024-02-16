class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        res = nums[0]  # Assume the first element is the minimum to start

        while L <= R:
            # If the subarray is already sorted, update res to the smallest in this subarray
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break  # The rest of the array is sorted, no need to search further
            
            m = (L + R) // 2
            res = min(res, nums[m])
            
            # Determine which side is sorted and adjust L or R accordingly
            if nums[m] >= nums[L]:
                # Left side is sorted, pivot must be in the right part
                L = m + 1
            else:
                # Right side is sorted, pivot must be in the left part
                R = m - 1

        return res

# If the value at the middle (mid) is greater than or equal to the value at the left pointer (L), the minimum element is to the right of mid.- So shift the L to m + 1
# If the value at mid is less than the value at L, the minimum element is to the left of mid.- So shift R to m - 1
# If the value at L is less than the value at the right pointer (R), the array is already sorted, and the minimum element is at L.
