class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create a list to keep track if a part of the string can make a word.
        dp = [False] * (len(s) + 1)
        # Mark the end as True to start checking from the back.
        dp[-1] = True

        # Start from the end of the string and move backwards.
        for i in range(len(s) - 1, -1, -1):
            # Try each word in the dictionary.
            for w in wordDict:
                # First we need to check if starting from i the string s has enough chars for w to be compared to it
                # Then check if it matches the word w.
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    # If it matches, mark the start of this word as True.
                    dp[i] = dp[i + len(w)]
                # If one word matches, no need to check the other words.
                if dp[i]:
                    break

        # Return True if the start of the string can start a word.
        return dp[0]
