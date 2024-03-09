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
