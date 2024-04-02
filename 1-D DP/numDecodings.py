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


# Eg- "126"
# dfs(0) - "126" returns 3
# ├── dfs(1) - "26" returns 2
# │   ├── dfs(2) - "6" [Decoding "2"] returns 1
# │   │   └── dfs(3) [Decoding "6"] returns 1
# │   └── dfs(3) [Decoding "26"] returns 1
# └── dfs(2) - "6" [Decoding "12"] returns 1
#     └── dfs(3) [Decoding "6"] returns 1

class Solution:
    def numDecodings(self, s: str) -> int:
        # If the first character is '0', it's invalid.
        if s[0] == '0':
            return 0
        
        n = len(s)  # The length of the string.
        dp = [0] * (n + 1)  # DP array to store the number of ways to decode up to each point.
        dp[0], dp[1] = 1, 1  # Base cases: one way to decode an empty string and a one-character string (if not '0').

        # Loop through the string starting from the second character.
        for i in range(2, n + 1):
            # Current single digit, can be '0' through '9'.
            one = int(s[i - 1])
            # Current pair of digits, can be '00' through '99'.
            two = int(s[i - 2:i])

            # If the single digit forms a valid character ('1' to '9'), 
            # it adds the same number of ways as up to the previous character.
            if 1 <= one <= 9:
                dp[i] += dp[i - 1]

            # If the pair of digits form a valid character ('10' to '26'), 
            # it adds the same number of ways as up to the character before the previous one.
            if 10 <= two <= 26:
                dp[i] += dp[i - 2]

        # The last element in dp array represents the total number of ways to decode the entire string.
        return dp[n]
