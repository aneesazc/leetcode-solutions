# Time- O(n * m)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            # Base case: Check if the cell is out of bounds or has been visited
            # before, or if its height is lower than the previous cell.
            if ((r, c) in visit or min(r, c) < 0
                or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return

            # Mark the current cell as visited
            visit.add((r, c))

            # Recurse into adjacent cells, passing the current height as `prevHeight`
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # DFS from cells along the top and left edges for the Pacific ocean
        for c in range(COLS):
            dfs(0, c, pac, 0)  # Passing 0 as prevHeight since we're starting from the ocean
        for r in range(ROWS):
            dfs(r, 0, pac, 0)  # Passing 0 as prevHeight since we're starting from the ocean

        # DFS from cells along the bottom and right edges for the Atlantic ocean
        for c in range(COLS):
            dfs(ROWS - 1, c, atl, 0)  # Passing 0 as prevHeight since we're starting from the ocean
        for r in range(ROWS):
            dfs(r, COLS - 1, atl, 0)  # Passing 0 as prevHeight since we're starting from the ocean

        # Compile results by finding cells reachable from both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res

