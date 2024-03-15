# Design a directed Graph class.
class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList and dst in self.adjList:
            if dst in self.adjList[src]:
                self.adjList[src].remove(dst)
                return True
            else:
                return False
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        def dfs(node, target, adjList, visit):
            if node in visit:
                return False
            if node == target:
                return True

            visit.add(node)
            for nei in adjList[node]:
                if dfs(nei, target, adjList, visit):
                    return True
            # visit.remove(node)

            return False

        return dfs(src, dst, self.adjList, set())

'''
In your hasPath function, "visit.remove(node)" is not needed because once a node is visited in the search from a specific source to a destination, 
there's no need to revisit it. The search aims only to find whether a path exists, not all possible paths, so unmarking nodes (removing them from the visited set) 
after visiting them is unnecessary for this specific goal.
'''

# Graph Implementation using Adjacency List
class Graph:
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        # If src or dst don't exist, add them
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        # Add edge if not already exists
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        # Check if src and dst exist in the graph
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        # Remove the edge
        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self._dfs(src, dst, visited)

    def _dfs(self, src: int, dst: int, visited: set) -> bool:
        if src == dst:
            return True
        visited.add(src)
        for neighbor in self.adj_list.get(src, []):
            if neighbor not in visited:
                if self._dfs(neighbor, dst, visited):
                    return True
        return False

    # Alternatively, use BFS for hasPath
    # def hasPathBFS(self, src: int, dst: int) -> bool:
    #     visited = set()
    #     queue = deque([src])
    #     while queue:
    #         curr = queue.popleft()
    #         if curr == dst:
    #             return True
    #         visited.add(curr)
    #         for neighbor in self.adj_list.get(curr, []):
    #             if neighbor not in visited:
    #                 queue.append(neighbor)
    #                 visited.add(neighbor)
    #     return False
