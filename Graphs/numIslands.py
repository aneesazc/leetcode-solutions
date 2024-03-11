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

'''
In the context of the numIslands problem, backtracking and removing from the visited set (as we might do in other backtracking problems) are not necessary. 
This distinction is due to the nature of the problem and the goal of the algorithm:

Problem Nature: The objective here is to count the number of disconnected islands on a grid. 
Once we have visited a cell, we are marking it as part of an island (by adding it to the visit set) and we will 
never need to "unmark" it because there is no concept of an incorrect path. Unlike in permutation or combination 
problems where we explore different possible configurations and backtrack to explore different paths after hitting a dead-end, 
here every path correctly contributes to identifying the extent of an island.

Visit Only Once: In the island counting problem, each cell represents part of land ('1') or water ('0'). 
Once a land cell is visited, we mark it to avoid counting it as part of another island. Since an island is 
defined as a group of adjacent lands surrounded by water, once we have explored and marked all land cells connected to a given land cell, 
we have completely defined the extent of that island. There is no need to reconsider these cells again, so they remain visited.

DFS Purpose: The depth-first search (DFS) here serves to explore and mark all cells belonging to the same island. 
After a cell and all its reachable land neighbors have been marked as visited, the algorithm moves on. 
There's no "wrong decision" to backtrack from because all connected lands form a single entity—an island. Each call to DFS explores one connected component (an island) fully.

Single Visit Logic: Since the purpose of the visit set is to keep track of cells that have already been accounted for as part of an island, 
once we add a cell to this set, it signifies that this part of the land has already been included in an island count, ensuring we do not double-count any part of an island.

Therefore, in the numIslands algorithm, once a land cell is visited and processed, there's no need to "undo" this action, 
because we're simply counting connected components (islands) and ensuring each cell is considered only once. 
The lack of a "backtrack and remove" step reflects the one-way progression of marking land cells: once a cell is determined to be part of an island, 
this fact never changes within the scope of the problem.
'''
