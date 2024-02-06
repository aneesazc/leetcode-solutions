# Time, Space - O(n), O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        window = set()

        for R in range(len(s)):
            # If s[R] is in window, we found a duplicate.
            # Remove characters from the left until s[R] can be added without duplicates.
            while s[R] in window:
                window.remove(s[L])
                L += 1
            # Now that we've ensured no duplicates, add the current character to the window.
            window.add(s[R])
            # Update the length of the longest substring without repeating characters.
            length = max(length, R - L + 1)

        return length
