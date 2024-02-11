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



'''
s = "abcabcbb"
Initial Window: As before, iterates through 'a', 'b', 'c', updating the window to {'a', 'b', 'c'} with res = 3.

Next Character 'a': Before adding the next 'a', it checks for duplicates.
Upon finding 'a' in the window, it correctly removes elements from the left just until it removes the duplicate 'a'. 
This means after the duplicate 'a' is removed, the next 'a' is added, making the window {'b', 'c', 'a'} after the first removal, 
and finally just {'a'} after removing 'b' and 'c' to accommodate the new 'a', 
with the correct res updating based on the longest unique substring encountered so far.

The loop ensures s[R] is added to the window only after ensuring any duplicate is removed, 
maintaining the invariant that the window always contains unique characters.

When encountering a character that already exists in the window, 
it removes characters from the left up until (and including) the first occurrence of the duplicate character, then adds the current character. 
This maintains a valid substring of unique characters and updates res accordingly.
'''
