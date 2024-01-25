# 1. Check if array contains a pair of duplicate values,
# where the two duplicates are no farther than k positions from 
# eachother (i.e. arr[i] == arr[j] and abs(i - j) + 1 <= k).
# O(n)
'''
for the condition arr[i] == arr[j] and abs(i - j) + 1 <= k), then window size will be k
'''
Solution- 
def closeDuplicates(nums, k):
    window = set() # Cur window of size <= k
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False

# 2. Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
# such that nums[i] == nums[j] and abs(i - j) <= k.

'''
for the condition arr[i] == arr[j] and abs(i - j) <= k), then window size will be k + 1
'''

 class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
                
            if nums[R] in window:
                return True

            window.add(nums[R])
        
        return False
