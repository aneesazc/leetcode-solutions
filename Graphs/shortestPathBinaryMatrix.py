from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # Check if the starting or ending cell is blocked.
        if grid[0][0] != 0 or grid[ROWS - 1][COLS - 1] != 0:
            return -1
        
        visit = set()
        q = deque()
        q.append((0, 0, 1))  # Append starting point with initial path length as 1
        visit.add((0, 0))
        directions = [
                [1, 0],   # Down
                [-1, 0],  # Up
                [0, 1],   # Right
                [0, -1],  # Left
                [1, 1],   # Down-Right
                [1, -1],  # Down-Left
                [-1, 1],  # Up-Right
                [-1, -1]  # Up-Left
            ]

        while q:
            r, c, length = q.popleft()  # Now, 'length' is part of the dequeued item
            if r == ROWS - 1 and c == COLS - 1:
                return length  # Return the length if we reach the bottom-right cell

            for dr, dc in directions:
                curR, curC = r + dr, c + dc
                if 0 <= curR < ROWS and 0 <= curC < COLS and grid[curR][curC] == 0 and (curR, curC) not in visit:
                    q.append((curR, curC, length + 1))  # Increase length as we move to the next cell
                    visit.add((curR, curC))

        # If the loop completes without returning, no path was found.
        return -1

'''
In your BFS implementation for the shortest path problem, the inclusion of the path length (length) as a third parameter 
within each queue element eliminates the need for an outer loop to process nodes level by level.

By appending the current path length to each cell during enqueuing (q.append((curR, curC, length + 1))), 
you're seamlessly integrating level-processing within the BFS structure itself, thereby making the outer for-loop used in some BFS implementations redundant. 
Each cell carries its "level" (in terms of path distance from the start) with it, providing all the information needed without additional layer-by-layer processing.
'''

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0, 0, 1)]) # r, c, length
        visit = set((0, 0))
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0],
                  [1, 1], [-1, -1], [1, -1], [-1, 1]]
        while q:
            r, c, length = q.popleft()
            if (min(r, c) < 0 or max(r, c) >= N or
                grid[r][c]):
                continue
            if r == N - 1 and c == N - 1:
                return length
            for dr, dc in direct:
                if (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))
        return -1

'''
Here’s how this approach works:

Queue Initialization: You start by adding the starting cell (0, 0) to the queue with a path length of 1, just like before. 
This is assuming implicitly that the starting cell is unblocked. If it is blocked, it will be caught by the grid check within the loop.

While Loop: Your main BFS loop begins without pre-checking if the starting or ending cell is open. Instead, you rely on the natural progression of the BFS to discover if these cells are blocked:
  If the starting cell (0, 0) is blocked, the first iteration of the loop will immediately continue due to grid[r][c] being true (since grid[0][0] would be 1 for a blocked cell). 
  Since no other cells will be enqueued before this check, the queue will quickly empty, and the method will return -1.
  
  If the ending cell (N-1, N-1) is blocked, this will not directly impact the BFS loop's initial checks, 
  but this cell will never be reached by the BFS due to being blocked or due to all paths to it being blocked. 
  Hence, no path will fulfill the condition to terminate the BFS with a success, resulting in the function eventually returning -1.

Boundary and Blockage Checks: By integrating the boundary and blockage checks into the loop (min(r, c) < 0 or max(r, c) >= N or grid[r][c]), 
you efficiently skip over any invalid or blocked cells without needing separate initial validations.

Continuation Condition: When iterating through possible moves, you continue to the next iteration of the while-loop whenever 
you encounter a cell that is out of bounds or blocked. This avoids adding such cells to the queue or treating them as part of a valid path.

This approach makes the code concise and utilizes the BFS structure to handle invalid scenarios (like blocked start/end cells) implicitly
'''

'''
Checking whether a cell has already been visited later in the for loop rather than immediately 
when dequeuing an item from the BFS queue is a design choice that can impact efficiency and readability. 
However, there are specific reasons and scenarios where this design might be applied:

Redundancy Reduction: When you directly dequeue a cell, you're only just beginning to consider its potential as a step in a path. 
By deferring the visited check to the point just before enqueueing the next steps, you reduce redundancy. 
This is because a cell might have been marked as visited after it was enqueued but before it was dequeued due to the nature of BFS exploring multiple paths concurrently.
'''
