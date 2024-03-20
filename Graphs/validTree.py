# using Union Find
'''
A valid tree with 'n' nodes must satisfy two conditions:

It must contain exactly 'n - 1' edges (any more, and it must contain at least one cycle; any less, and it cannot be fully connected).
It must be acyclic (i.e., it must not contain any cycles).

You can use the Union-Find algorithm to check both of these conditions
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]  # Parent array for Union-Find
        rank = [1] * n  # Rank array for Union-Find

        def find(n1):
            # Find root of n1 with path compression
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]  # Path compression step
                res = par[res]
            return res

        def union(n1, n2):
            # Union by rank; return 0 if n1 and n2 are already connected (which means a cycle is found)
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0

            # Union by rank
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        # Variable 'total' is supposed to track the number of unique sets (connected components)
        total = n
        
        for n1, n2 in edges:
            if union(n1, n2) == 0:  # If a cycle is found
                return False
            total -= 1  # Decrease number of unique sets for each successful union

        # Check if exactly one connected component remains and if the number of edges is n - 1
        return total == 1 and len(edges) == n - 1


'''
The return value at the end is modified to ensure that two conditions are met: there is exactly one connected component (implying the graph is fully connected), 
and the number of edges is exactly n - 1 (implying no cycles for an undirected graph, which also meets the requirement for the graph being a tree).

This solution properly checks both for the absence of cycles (via the union-find checks) and for connectivity (ensuring that all nodes are connected and the number of edges is exactly n - 1).
'''


