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



#  Time: O(2^(n + m)), Space: O(n + m)
def dfs(s1, s2):
    return dfsHelper(s1, s2, 0, 0)

def dfsHelper(s1, s2, i1, i2):
    if i1 == len(s1) or i2 == len(s2):
        return 0
    
    if s1[i1] == s2[i2]:
        return 1 + dfsHelper(s1, s2, i1 + 1, i2 + 1)
    else:
        return max(dfsHelper(s1, s2, i1 + 1, i2),
                dfsHelper(s1, s2, i1, i2 + 1))


# Time: O(n * m), Space: O(n + m)
def memoization(s1, s2):
    N, M = len(s1), len(s2)
    cache = [[-1] * M for _ in range(N)]
    return memoHelper(s1, s2, 0, 0, cache)

def memoHelper(s1, s2, i1, i2, cache):
    if i1 == len(s1) or i2 == len(s2):
        return 0
    if cache[i1][i2] != -1:
        return cache[i1][i2]

    if s1[i1] == s2[i2]:
        cache[i1][i2] = 1 + memoHelper(s1, s2, i1 + 1, i2 + 1, cache)
    else:
        cache[i1][i2] = max(memoHelper(s1, s2, i1 + 1, i2, cache),
                memoHelper(s1, s2, i1, i2 + 1, cache))
    return cache[i1][i2]


# Time: O(n * m), Space: O(n + m)
def dp(s1, s2):
    N, M = len(s1), len(s2)
    dp = [[0] * (M+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(M):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[N][M]
