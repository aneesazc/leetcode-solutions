# brufe force dp dfs
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1  # Correct target to be the last index of the array

        def dfs(i):
            # Base case: if current index reaches or exceeds the target, return True
            if i >= target:
                return True
            
            # Recursive call: try to jump from current index to the furthest possible index
            furthest_jump = min(i + nums[i], target)  # Limit jump to within bounds
            for j in range(furthest_jump, i, -1):  # Start from furthest possible jump to use greedy approach
                if dfs(j):
                    return True
            return False

        return dfs(0)


# greedy approach- 0(n) time
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i

        return True if goal == 0 else False 


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize 'goal' to the last index of the array.
        goal = len(nums) - 1

        # Traverse the list backwards starting from the second last element.
        for i in range(len(nums) - 2, -1, -1):
            # Check if the current position 'i' combined with the jump length at 'i'
            # can reach or exceed the current 'goal'.
            if nums[i] + i >= goal:
                # If it can reach or pass the goal, update the goal to be the current position 'i'.
                # This means we can now consider reaching this new goal as the next sub-goal.
                goal = i

        # After the loop, if the goal is 0, it means we can jump from the start to the end of the array.
        return goal == 0
