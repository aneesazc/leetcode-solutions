# O (amount * len(coins))
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # idx(coins) maps to -> min no. coins to sum to idx coins
        dp[0] = 0 # base case: 0 coins make up to 0 amount

        for a in range(1, amount + 1): # 1, 2, 3,...7
            for c in coins: # [1, 3, 4, 5]
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c]) # 1 comes from current coin c
        return dp[amount] if dp[amount] != amount + 1 else -1

'''
In dp[a] = min(dp[a], 1 + dp[a - c]), the 1 represents using one coin. 
So, this formula checks if using one more coin (+1) plus the fewest coins 
needed for a smaller amount (a - c) gives you a smaller total than what you already have for amount a. 
It's like asking, "Is adding this coin going to make the total number of coins used less than before?"
'''
