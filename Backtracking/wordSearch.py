# Time- O(n * m * dfs) 4^len(word) -> O(n * m * 4^n)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()  # A set to keep track of visited cells to avoid revisiting

        def dfs(r, c, i):
            # Base case: all characters matched
            if i == len(word):
                return True

            # Out of bounds, character mismatch, or cell already visited
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path:
                return False

            path.add((r, c))  # Mark this cell as visited

            # Explore all possible directions: down, up, right, left
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))

            path.remove((r, c))  # Unmark this cell for backtracking
            return res

        # Start from every cell
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):  # If true, word found
                    return True

        return False  # No valid path found for the word


'''
When the dfs function is called, it checks whether the current path through the board matches the word we are looking for, character by character. 
The variable i represents the index in the word word that we are currently trying to match on the board.

Incrementing i: Each time a character matches (i.e., word[i] == board[r][c]), 
the dfs function is called recursively to check the next character (i + 1) from the surrounding cells. 
This means that every time dfs is called, it is intended to validate the match for the next character in the word.

Reaching the end of the word: If at any point, i == len(word), this means that all characters from word[0] to word[i-1] 
have successfully been matched in the correct sequence on the board. Remember, i is incremented after a successful character match, 
so if i equals the length of the word, it indicates that all preceding characters have been matched successfully.

No need for an additional board check at this point: By the time i equals the length of the word, we've already confirmed 
that each character up to i-1 is present on the board and arranged in the correct sequence (since each character match leads to an increment in i). 
There's no additional character to check on the board because i corresponds to a position beyond the last character of the word.

In essence, this base case acts as a successful termination condition for the recursive search: 
if we've incremented i enough times without violating any of the failure conditions (character mismatch, going out of bounds, revisiting a cell), 
then we must have found a valid path through the board that spells out the entire word, hence a complete match.
'''
