# Time, Space-  O(n), O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Check to see if a n is seq by seeing if n - 1 exists in nums, if n - 1 exists it means n is not a sequence and we can ignore it
# Next check if n + 1, n + 2, n + 3... exist in nums and then increase their curr length, compare it longest seq until then
# Do this for every sequence
