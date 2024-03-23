# Given a directed acyclical graph, return a valid
# topological ordering of the graph. 
def topologicalSort(edges, n):
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []
    for src, dst in edges:
        adj[src].append(dst)

    topSort = []
    visit = set()
    for i in range(1, n + 1):
        dfs(i, adj, visit, topSort)
    topSort.reverse()
    return topSort

def dfs(src, adj, visit, topSort):
    if src in visit:
        return
    visit.add(src)
    
    for neighbor in adj[src]:
        dfs(neighbor, adj, visit, topSort)
    topSort.append(src)


# Given a directed graph, perform a topological sort on its vertices and return the order as a list of vertex labels
# If the graph contains a cycle, you should return an empty list to indicate that a topological sort is not possible.
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        topSort = []
        visited = set()  # Visited nodes
        visiting = set() # Nodes being visited in the current DFS call (used to detect cycles)
        
        def dfs(src: int) -> bool:
            if src in visited:
                return True
            if src in visiting:
                return False  # A cycle is detected

            visiting.add(src)
            
            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False  # A cycle is detected
                
            visiting.remove(src)
            visited.add(src)
            topSort.append(src)
            
            return True  # No cycle detected

        for i in range(n):
            if not dfs(i):
                return []  # Return an empty list if a cycle is detected
        
        topSort.reverse()
        return topSort
