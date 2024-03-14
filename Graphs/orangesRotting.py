# Time- O(n * m)
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        
        # Initialize the queue with all initially rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))  # Add minute count as third param

        minute = 0  # Track the last minute count after BFS
        while q:
            r, c, minute = q.popleft()  # Dequeue and unpack the minute value
            
            # Explore the four possible directions from the current cell
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc  # New row and column
                # Check bounds and whether the orange is fresh
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Rot the fresh orange
                    q.append((nr, nc, minute + 1))  # Add to queue with incremented minute
        
        # After BFS, check if there are still fresh oranges left
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1  # Not all oranges have rotted

        return minute  # Return the last minute count from the BFS


'''
In the "oranges rotting" problem:

Initialization: Instead of starting from (0,0), you typically start with all initially rotten oranges (marked as '2' in the grid). These form the initial layer or wave of the BFS.

BFS Process: The BFS expands from all rotten oranges simultaneously, checking their adjacent cells and rotting fresh oranges (marked as '1'). The rotting spreads by one unit of distance per minute.

End Condition: The process continues until either there are no more fresh oranges to rot (success), or it is impossible to rot all fresh oranges due to isolation (failure).


In the "oranges rotting" problem, you don't need a separate visit set because the grid itself tracks the state of each cell: 
it indicates whether a cell contains a fresh orange (1), a rotten orange (2), or is empty (0). 
This usage of the grid's values to track progress and state effectively replaces the need for a separate set to keep track of visited cells.
'''

'''
There will be a different copy of a minute count for every rotten orange right? How does the global minute value know which minute count to return?

TLDR: In summary, the 'global' minute value you return at the end of the BFS process is the time stamp of the last orange processed, 
which represents the maximum time taken to rot all reachable oranges. 


Here's how it works:
Individual Time Stamps: When an orange rots, it is added to the queue with a time stamp, 
which is essentially the current minute count when that orange became rotten. 
This count is not global but specific to the path through which the rot reached that particular orange.

BFS Expansion: As the BFS progresses, it dequeues oranges from the queue, explores their neighbors, 
and enqueues any fresh neighbors as newly rotten—each with a time stamp incremented by one from the dequeued orange. 
This means that each layer of the BFS (each set of oranges that can be reached in the same number of steps from the 
initial layer of rotten oranges) is associated with a specific minute count.

Global Minute Tracking: The 'global' minute count, in this context, refers to the maximum minute count seen during the BFS process. 
This is not tracked by a separate variable but rather is reflected in the minute count associated with each orange as it is processed. 
Since the BFS processes cells in order from earliest to latest in terms of their rotting time, 
the last orange to rot (which would be processed last by the BFS) carries the highest minute count.

End of Process: When the BFS concludes (either because the queue is empty or because the algorithm has finished processing all cells), 
the highest minute count encountered (which corresponds to the furthest reach of rot from the initial rotten oranges, 
in terms of time) is inherently the value of the last dequeued orange's time stamp. This is the total time required for the rot to spread to all reachable oranges.
'''
