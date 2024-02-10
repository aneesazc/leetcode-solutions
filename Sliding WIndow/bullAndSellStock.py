# Time, Space - O(n), O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0  # Maximum profit
        L = 0  # Left pointer initialized at the start

        # Iterate through prices with right pointer
        for R in range(1, len(prices)):
            # If the current price is lower than the price at L, it means we have found a new lower price to buy at.
            # Therefore, we move L to R because buying at the current price (R) would allow for a potentially higher profit in the future
            # than continuing with the higher buy price at L. This is because we aim to maximize the profit by minimizing the buy price.
            if prices[R] < prices[L]:
                L = R # we found a new low(which is prices[R])? we buy at that price now for maximum profit by moving L to R
            else:
                # Calculate current profit and update maxP if it's higher
                currP = prices[R] - prices[L]
                maxP = max(maxP, currP)

        return maxP





class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L = 0

        for R in range(len(prices)):
            currProf = prices[R] - prices[L]
            if currProf <= 0:
                L = R
            else:
                res = max(res, currProf)

        return res




class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res

            
