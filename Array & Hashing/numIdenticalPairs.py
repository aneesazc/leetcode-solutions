class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Initialize the result variable to store the total count of good pairs
        res = 0
        # Initialize a dictionary to keep count of each number's occurrences in nums
        count = {}
        # Iterate through each number in nums
        for n in nums:
            # If the number has already been seen,
            # its current count in 'count' is the number of good pairs it can form with this occurrence
            if n in count:
                # Add the current count of n to res since each occurrence of n before this
                # can form a good pair with this occurrence
                res += count[n]
                # Increment the count for this number as we've encountered it again
                count[n] += 1
            else:
                # If it's the first time we've seen this number, initialize its count to 1
                count[n] = 1
        # Return the total count of good pairs
        return res
