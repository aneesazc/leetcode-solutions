# DFS solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check for an empty grid or grid with empty rows, return 0 as there are no islands.
        if not grid or not grid[0]:
            return 0

        # Initialize counter for islands and a set to track visited cells.
        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])  # Get the dimensions of the grid.

        # Define the depth-first search (DFS) function.
        def dfs(r, c):
            # Return if out of bounds, already visited, or water ('0').
            if (r < 0 or c < 0 or r == rows or c == cols or 
                (r, c) in visit or grid[r][c] == "0"):
                return

            # Mark the current cell as visited.
            visit.add((r, c))

            # Directions to move in the grid: right, left, down, up.
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            # Explore all connected cells (part of the same island).
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Loop through each cell in the grid.
        for r in range(rows):
            for c in range(cols):
                # If the cell is land ('1') and not visited, it's part of a new island.
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1  # Increment islands count.
                    dfs(r, c)  # Start DFS from this cell to mark all connected land.

        # Return the total number of islands found.
        return islands


'''
This code works by scanning each cell in the grid; when it finds a piece of land (denoted as '1') that hasn't been visited, 
it triggers a DFS search starting from that cell. The DFS will mark all adjacent (horizontally or vertically) land cells as visited. 
This process groups all connected land cells into a single island and ensures each piece of land is counted only once towards the total number of islands.
'''
