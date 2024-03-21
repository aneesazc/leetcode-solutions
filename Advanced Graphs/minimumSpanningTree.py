import heapq
# Implementation for Prim's algorithm to compute Minimum Spanning Trees
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst, w in edges:
            adj[src].append([dst, w])
            adj[dst].append([src, w])

        totalW = 0 # Total weight of the MST
        visit = set()
        visit.add(0)
        minHeap = []

        for nei, w in adj[0]: # start bfs at neighbors of 0
            heapq.heappush(minHeap, [w, 0, nei])

        while minHeap:
            w, src, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            totalW += w
            visit.add(node)
            for nei, w in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, [w, node, nei])
                  
        # Return -1 if not all nodes are visited (unconnected graph)
        return totalW if len(visit) == n else -1 

