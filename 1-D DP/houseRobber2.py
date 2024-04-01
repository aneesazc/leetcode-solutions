class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:  # If there's only one house, return its value.
            return nums[0]

        # First scenario: Exclude the last house.
        rob1, rob2 = 0, 0
        for i in range(0, len(nums) - 1):
            # At each step, decide between robbing the current house + amount from two steps back
            # and not robbing it (taking the amount from one step back).
            curr = max(nums[i] + rob1, rob2)
            rob1 = rob2  # Move the window forward for the next iteration.
            rob2 = curr

        # Second scenario: Exclude the first house.
        rob3, rob4 = 0, 0
        for i in range(1, len(nums)):
            curr = max(nums[i] + rob3, rob4)
            rob3 = rob4  # Again, move the window forward.
            rob4 = curr

        # The final answer is the maximum amount robbed between the two scenarios.
        return max(rob2, rob4)



class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
