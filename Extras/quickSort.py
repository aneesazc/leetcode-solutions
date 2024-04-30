def quick_sort(nums, low, high):
    if low < high:
        # Partition the array and get the pivot index
        i = partition(nums, low, high)

        # Corrected range for recursive calls
        quick_sort(nums, low, i - 1)  # Sort left of the pivot (not include pivot becuase it's already in sorted pos)
        quick_sort(nums, i + 1, high)  # Sort right of the pivot (again not include pivot)


def partition(nums, low, high):
    # Choose the last element as the pivot
    pivot = nums[high]

    i = low  # Pointer for the smaller element

    for j in range(low, high):
        if nums[j] < pivot:
            # Swap smaller element with nums[i]
            nums[i], nums[j] = nums[j], nums[i]
            i += 1  # Move the pointer forward

    # Swap pivot into correct position
    nums[i], nums[high] = nums[high], nums[i]

    return i  # Return the pivot index

# Example usage:
nums = [10, 7, 8, 9, 1, 5]
quick_sort(nums, 0, len(nums) - 1)
print(nums)  # Expected: [1, 5, 7, 8, 9, 10]
