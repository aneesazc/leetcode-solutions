class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialize parent array, each node is its own parent at the beginning
        par = [i for i in range(n)]
        # Initialize rank array, used for union by rank, start with all nodes having rank 1
        rank = [1] * n

        def find(n1):
            # Find the root of the node 'n1' with path compression
            res = n1
            while res != par[res]:
                # Path compression step, make every node on the path point to its grandparent
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            # Connect two nodes n1 and n2, return 1 if they were disconnected before, otherwise return 0
            p1, p2 = find(n1), find(n2)
            if p1 == p2:  # Already connected, no new components formed
                return 0

            # Union by rank: attach the smaller tree under the root of the larger tree
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]  # Increase the rank of the root of the larger tree
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1  # New connection formed, so we return 1

        # Start with 'n' isolated components
        total = n
        # For each edge, try to connect the two nodes, and decrease the total number of components if successful
        for n1, n2 in edges:
            total -= union(n1, n2)

        # Return the total number of connected components at the end
        return total




