from collections import defaultdict 

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        # Here, for a pair [a, b], 'a' must be taken before 'b', 
        # but we represent it such a way 'b' as the crs and 'a' as the prerequisite as it's easier this way
        # if this is confusing check next solution
        for pre, crs in prerequisites:
            adj[crs].append(pre)

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for pre in adj[crs]:
                    prereqMap[crs] |= dfs(pre) # union
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        prereqMap = {} # map crs -> set of indirect prereqs
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res


from collections import defaultdict 

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        # Here we represer [pre, crs] the usual way just switch v and u order below
        for pre, crs in prerequisites:
            adj[pre].append(crs)

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for pre in adj[crs]:
                    prereqMap[crs] |= dfs(pre) # union
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        prereqMap = {} # map crs -> set of indirect prereqs
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(v in prereqMap[u]) # v in prereqMap[u] 
        return res
