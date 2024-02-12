# Time- O(26n)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Dictionary to store the frequency of each character in the current window
        L = 0  # Initialize left pointer of the window
        res = 0  # Result variable to store the maximum length of the valid window

        for R in range(len(s)):  # Iterate over the string with the right pointer
            # Update the count of the current character
            count[s[R]] = 1 + count.get(s[R], 0)
            
            # If the current window size minus the highest frequency character exceeds k,
            # it means we have to replace more than k characters to make all characters in the window the same.
            # Therefore, we need to shrink the window from the left.
            if (R - L + 1) - max(count.values()) > k:
                count[s[L]] -= 1  # Decrement the count of the character at the left pointer
                L += 1  # Move the left pointer to the right

            # Update the result with the maximum length of the window encountered so far
            res = max(res, R - L + 1)
        
        return res  # Return the maximum length of the window found



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       L = 0
       res = 0
       count = {}

       for R in range(len(s)):
           count[s[R]] = 1 + count.get(s[R], 0)
           if (R - L + 1) - max(count.values()) <= k:
               res = max(res, R - L + 1)
           else:
                count[s[L]] -= 1
                L += 1

       return res
