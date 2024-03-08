class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []  # This list will store all the unique combinations that sum up to the target

        # Define the backtrack function that will be used to find all combinations
        def backtrack(i, curComb, total):
            # Base case: if the total equals the target, add a copy of the current combination to the results
            if total == target:
                combs.append(curComb.copy())
                return
            # If the current index is out of bounds or the total exceeds the target, stop the recursion
            if i >= len(candidates) or total > target:
                return

            # Include the current candidate in the combination and explore further
            curComb.append(candidates[i])
            backtrack(i, curComb, total + candidates[i])  # Recurse with the same index because we can use the same number multiple times

            # Backtrack: remove the last element added and explore the next candidate
            curComb.pop()
            backtrack(i + 1, curComb, total)  # Move to the next candidate, keeping the current total

        # Start the backtracking from the first index, an empty combination, and a total of 0
        backtrack(0, [], 0)
        return combs  # Return the list of all unique combinations found



'''
Let's break down the two parts:

backtrack(i, curComb, total + candidates[i]): In this line, you're calling the backtrack function recursively, including the current candidate number (candidates[i]) in the total. 
Here, i remains the same because, in this problem, you're allowed to use the same number as many times as you want until you reach or exceed the target sum. 
This is why i doesn't change in this recursive call—you're exploring all possibilities that include multiple instances of candidates[i]. 
You're essentially saying, "What happens if I add this number one more time?"

backtrack(i + 1, curComb, total): After the previous step, where you explored the possibility of including candidates[i], 
you now explore the possibility of not including candidates[i] any further in the combination. 
This is why curComb.pop() is called—to remove the last element that was added, which is candidates[i], 
because you're now moving on to check combinations without it. In this call, you're moving to the next candidate (i + 1), 
but the total sum doesn't change because you're not adding the next candidate yet; you're just preparing to explore combinations that start with the next candidate. 
This step essentially represents a decision not to include candidates[i] anymore and see whether any valid combinations can be formed with the remaining candidates.
'''
