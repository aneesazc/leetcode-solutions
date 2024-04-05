# most optimized
# Time O(n * m), Space- O(min(n, m))
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)

        # Ensure dp array uses the smaller dimension for space optimization
        if N < M:
            text1, text2 = text2, text1  # Swap to ensure text1 is always the longer string
            N, M = M, N  # Swap lengths to match swapped strings

        dp = [0] * (M + 1)

        for i in range(N):
            curRow = [0] * (M + 1)
            for j in range(M):
                if text1[i] == text2[j]:
                    curRow[j + 1] = 1 + dp[j] # add the diagonal top left LCS val
                else:
                    curRow[j + 1] = max(dp[j + 1], curRow[j]) # max of top and left LCS val
            dp = curRow

        return dp[M]
