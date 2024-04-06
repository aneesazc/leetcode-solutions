class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        
        N, M = len(s), len(t)
        dp = [0] * (M + 1)

        for i in range(N):
            curRow = [0] * (M + 1)
            for j in range(M):
                if s[i] == t[j]:
                    curRow[j + 1] = 1 + dp[j]
                else:
                    curRow[j + 1] = max(dp[j + 1], curRow[j])

            dp = curRow

        return dp[M]

# If two strs are palindromes their LCS will also always be their longest palindromic subsequence
# s = "bbbab"
# If we reverse s to say t = "babbb" the LCS of the two will also 
# be the longest palindromic subsequence since they are the same strs reversed
