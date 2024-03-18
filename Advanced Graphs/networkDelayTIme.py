import heapq 

class Solution:
    # basically return the max of all the shortest paths from the given source node
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {} 

        # Initialize the adjacency list with empty lists for each node
        for i in range(1, n + 1):
            adj[i] = []

        # Populate the adjacency list with directed edges from the input
        # u = source, v = destination, w = weight
        for u, v, w in times:
            adj[u].append([v, w])

        shortest = {}  # Dictionary to store the shortest time to each node from the starting node
        minHeap = [[0, k]]  # Priority queue (min heap), initialized with [time, node] for the starting node
        minVal = 0  # Track the maximum time taken to reach a node

        # Run Dijkstra's algorithm using the min heap
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)  # Pop the node with the smallest time
            if n1 in shortest:  # Skip this node if it has already been visited
                continue
            minVal = max(minVal, w1)  # Update the max time taken to reach a node
            shortest[n1] = w1  # Mark this node as visited with the shortest time

            # Iterate through all adjacent nodes of the current node
            for n2, w2 in adj[n1]:
                if n2 not in shortest:  # If the adjacent node hasn't been visited yet
                    heapq.heappush(minHeap, [w1 + w2, n2])  # Add it to the heap with updated time

        # Check if all nodes have been reached
        for i in range(1, n + 1):
            if i not in shortest:  # If any node hasn't been reached, return -1
                return -1
        
        return minVal  # Return the maximum time taken to reach the last node


# more optimised
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for u, v, w in times:
            adj[u].append([v, w])

        shortest = {} # or set()
        minHeap = [[0, k]]
        res = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            res = max(res, w1)
            shortest[n1] = w1 # or shortest.add(n1) since we don't really need to save the shortest path from every node in final solution

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])

        if len(shortest) != n:
            return -1

        # basically the max of all the shortest paths from the given source node
        return res # final solution only contains maximum time it takes for any node to receive the signal from the given source node
        
