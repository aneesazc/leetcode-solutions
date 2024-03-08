class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []  # This will store all unique permutations
        perm = []  # Current permutation
        count = {}  # Dictionary to count occurrences of each number in nums
        for n in nums:
            count[n] = 1 + count.get(n, 0)  # Populate count dictionary
        
        def dfs():
            if len(perm) == len(nums):  # Base case: if permutation is complete
                res.append(perm.copy())  # Add a copy of the complete permutation to the result
                return

            for n in count:  # Iterate through all unique numbers
                if count[n] > 0:  # Check if the number can be used in the permutation
                    perm.append(n)  # Add number to the current permutation
                    count[n] -= 1  # Decrement the count of that number

                    dfs()  # Recursively call dfs to continue building the permutation

                    count[n] += 1  # Increment the count back after backtracking
                    perm.pop()  # Remove the number from the current permutation (backtrack)

        dfs()
        return res
