class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp




class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)  # Initialize list with zeros up to n

        for i in range(1, n + 1):
            # Use the relationship: countBits[i] = countBits[i >> 1] + (i & 1)
            ans[i] = ans[i >> 1] + (i & 1)

        return ans
