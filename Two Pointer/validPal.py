class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L < R:
            # Skip non-alphanumeric characters from the left
            while L < R and not s[L].isalnum():
                L += 1

            # Skip non-alphanumeric characters from the right
            while L < R and not s[R].isalnum():
                R -= 1

            # Compare characters case insensitively
            if s[L].lower() != s[R].lower():
                return False

            # Move both pointers towards the center
            L += 1
            R -= 1

        return True
