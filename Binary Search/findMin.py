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
