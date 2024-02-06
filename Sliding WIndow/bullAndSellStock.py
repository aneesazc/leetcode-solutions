# Time, Space - O(n), O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0  # Maximum profit
        L = 0  # Left pointer initialized at the start

        # Iterate through prices with right pointer
        for R in range(1, len(prices)):
            # If current price is lower than prices[L], move L to R
            if prices[R] < prices[L]:
                L = R
            else:
                # Calculate current profit and update maxP if it's higher
                currP = prices[R] - prices[L]
                maxP = max(maxP, currP)

        return maxP
