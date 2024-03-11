# Time and Space- O(n * m)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        maxArea = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])  

        def dfs(r, c):
            # Return area 0 if out of bounds, cell already visited, or is water (0).
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or grid[r][c] == 0:
                return 0

            # Mark the cell as visited.
            visit.add((r, c))

            # Count the current cell, then explore all adjacent cells (up, down, left, right)
            # and sum their areas. This recursion accumulates the area of the island.
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        # Iterate over every cell in the grid.
        for r in range(rows):
            for c in range(cols):
                # Start a new island traversal only if the cell is land (1) and not visited.
                if grid[r][c] == 1 and (r, c) not in visit:
                    # Calculate the area for the new island.
                    currArea = dfs(r, c)
                    # Update the maximum area found so far.
                    maxArea = max(maxArea, currArea)
                  
        # Return the largest island's area found in the entire grid.
        return maxArea

        # Return the largest island's area found in the entire grid.
        return maxArea
