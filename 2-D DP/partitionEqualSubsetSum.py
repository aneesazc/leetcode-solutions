# brtue force
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        # If the total sum is odd, it's impossible to partition into two equal subsets
        if total_sum % 2 != 0:
            return False
        target_sum = total_sum // 2
        
        def dfs(i, cur_sum):
            # Base case: if current sum equals target_sum, a partition is found
            if cur_sum == target_sum:
                return True
            # If index is out of bounds or current sum exceeds target_sum, no valid partition
            if i == len(nums) or cur_sum > target_sum:
                return False
            # Recursive call to try including nums[i] in the current subset or excluding it
            # Include nums[i] in the subset
            if dfs(i + 1, cur_sum + nums[i]):
                return True
            # Exclude nums[i] from the subset
            return dfs(i + 1, cur_sum)
        
        # Start the DFS from index 0 with a current sum of 0
        return dfs(0, 0)


# momoized
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        # If the total sum is odd, it's impossible to partition into two equal subsets
        if total_sum % 2 != 0:
            return False
        target_sum = total_sum // 2

        # Initialize the memoization table with None, indicating uncomputed states
        # The table dimensions are N x (target_sum + 1), where N is the number of items
        memo = [[None for _ in range(target_sum + 1)] for _ in range(len(nums))]

        def dfs(i, cur_sum):
            # Base case: if current sum equals target_sum, a partition is found
            if cur_sum == target_sum:
                return True
            # If index is out of bounds or current sum exceeds target_sum, no valid partition
            if i == len(nums) or cur_sum > target_sum:
                return False
            # If this subproblem has already been solved, return the cached result
            if memo[i][cur_sum] is not None:
                return memo[i][cur_sum]
            # Recursive call to try including nums[i] in the current subset or excluding it
            # Store the result in the memo table before returning it
            # Include nums[i] in the subset
            include = dfs(i + 1, cur_sum + nums[i])
            # Exclude nums[i] from the subset
            exclude = dfs(i + 1, cur_sum)
            memo[i][cur_sum] = include or exclude
            return memo[i][cur_sum]
        
        # Start the DFS from index 0 with a current sum of 0
        return dfs(0, 0)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        target_sum = total_sum // 2
        memo = [[None for _ in range(target_sum + 1)] for _ in range(len(nums))]
        
        def dfs(i, cur_sum):
            if cur_sum == target_sum:
                return True
            if i == len(nums) or cur_sum > target_sum:
                return False
            if memo[i][cur_sum] is not None:
                return memo[i][cur_sum]
            
            memo[i][cur_sum] = dfs(i + 1, cur_sum) or dfs(i + 1, cur_sum + nums[i])
            return memo[i][cur_sum]
        

        return dfs(0, 0)

# true dp bottom up to save space
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # If the total sum is odd, it's not possible to split the array into two subsets with equal sum
        if total_sum % 2 != 0:
            return False

        # Calculate the target sum each subset must reach (half of the total sum)
        target = total_sum // 2

        # Initialize a set to keep track of the sums that can be formed with the current subsets
        dp = set()
        # Start with a subset sum of 0 (base case)
        dp.add(0)
        
        # Iterate through each number in the array in reverse
        for i in range(len(nums) - 1, -1, -1):
            # Prepare a new set for the next state Because a set size cant change during iteration
            nextDP = set()
            # Check each sum in the current set
            for n in dp:
                # If the current sum is equal to the target, we found a subset that works
                if n == target:
                    return True
                # Add the current number to the current sum and add it to the next state
                nextDP.add(nums[i] + n)
                # Also carry forward the current sum without adding the current number
                nextDP.add(n)
            # Move to the next state
            dp = nextDP

        # After processing all numbers, check if the target sum is in our set of achievable sums
        return True if target in dp else False

