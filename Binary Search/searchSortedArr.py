# O(log n) obviously
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0  # Initialize left pointer to start of the array
        R = len(nums) - 1  # Initialize right pointer to end of the array

        while L <= R:  # Continue searching while this condition holds
            mid = (L + R) // 2  # Find the midpoint for binary search
            
            if nums[mid] == target:  # If the midpoint is the target, return its index
                return mid

            # If the middle element is greater than or equal to the left element, 
            # it indicates that the left portion is sorted and we are in the left potion
            if nums[mid] >= nums[L]: 
                # Target is not in the sorted range if it's greater than mid element 
                # or less than the left-most element
                if target > nums[mid] or target < nums[L]:
                    L = mid + 1  # Target must be in the right portion; adjust L accordingly
                else: # if target is lesser than mid but greater than left-most element
                    R = mid - 1  # Target is within the left sorted portion; adjust R

            # If the middle element is less than the left element, 
            # it indicates that the right portion is sorted
            else: 
                # Target is not in the sorted range if it's less than the mid element
                # or greater than the right-most element
                if target < nums[mid] or target > nums[R]:
                    R = mid - 1  # Target must be in the left portion; adjust R
                else:
                    L = mid + 1  # Target is within the right sorted portion; adjust L

        # If the loop ends without returning, the target is not in the array
        return -1



# more intuitive solution although much more logic and code
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0  # Start of the array
        R = len(nums) - 1  # End of the array

        while L <= R:
            mid = (L + R) // 2  # Middle index
            if nums[mid] == target:  # Target found
                return mid

            # Left portion is sorted and we are in the left portion
            if nums[mid] >= nums[L]:
                # Target is beyond mid
                if target > nums[mid]:
                    L = mid + 1  # Search right cause everything to the left is less than mid
                # Target is between L and mid
                elif target < nums[mid]:
                    if target < nums[L]:
                        L = mid + 1  # Search right 
                    else:
                        R = mid - 1  # Search left cause everything to the right is greater than mid

            # Right portion is sorted and we are in the right portion
            else:
                # Target is less than mid
                if target < nums[mid]:
                    R = mid - 1  # Search left
                # Target is beyond mid
                elif target > nums[mid]:
                    if target > nums[R]:
                        R = mid - 1  # Search left
                    else:
                        L = mid + 1  # Search right

        return -1  # Target not found

