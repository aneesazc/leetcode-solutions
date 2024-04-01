class Solution:
    def numDecodings(self, s: str) -> int:
        # Base case: one way to decode an empty string
        dp = {len(s): 1}

        def dfs(i):
            # If this subproblem has already been solved, return the solution
            if i in dp:
                return dp[i]
            
            # If the current character is '0', it cannot be decoded
            if s[i] == "0":
                return 0

            # Decode the current character on its own
            res = dfs(i + 1)
            
            # If the next character exists and the two characters form a valid letter
            # (either "1x" or "2x" where x <= "6"), add the ways to decode this pair
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            
            # Save the result in the memoization table
            dp[i] = res
            return res

        return dfs(0)
