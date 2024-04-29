def merge_sort(nums):
    if len(nums) < 2:
        return nums
    l = 0
    r = len(nums) - 1
    mid = (l + r) // 2
    # Change 1: Correct slicing to include all elements up to mid
    left_half = merge_sort(nums[l:mid + 1])
    # Change 2: Correct slicing to start at mid
    right_half = merge_sort(nums[mid + 1:r + 1])
    return merge(left_half, right_half)


def merge(first, second):
    new_list = []
    i, j = 0, 0
    # Change 3: Use indices instead of direct list checking
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            new_list.append(first[i])
            i += 1
        else:
            new_list.append(second[j])
            j += 1

    # Change 4: Append remaining elements directly
    new_list.extend(first[i:])
    new_list.extend(second[j:])
    
    return new_list



def merge_sort(nums):
    if len(nums) < 2:
        return nums
    first = merge_sort(nums[: len(nums) // 2])
    second = merge_sort(nums[len(nums) // 2 :])
    return merge(first, second)


def merge(first, second):
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final

'''
MERGE_SORT() IMPLEMENTATION
Input: A, a list of integers

If the length of A is less than 2, it's already sorted so return it
Split the input array into two halves down the middle
Call merge_sort() twice, once on each half
Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls
MERGE() IMPLEMENTATION
Inputs: A, B. Two lists of integers

Create a new "final" list of integers.
Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
Use a loop to iterate over A and B at the same time. If an element in A is less than or equal to its respective element in B, add it to the final list and increment i. 
Otherwise, add the item in B to the final list and increment j.
After comparing all the items, there may be some items left over in either A or B (if one of the lists is longer than the other). Add those extra items to the final list.
Return the final list.
'''
