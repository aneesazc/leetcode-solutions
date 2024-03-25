# O (E + V)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # a course has 3 possible states
        # visited -> course has been added to output
        # visiting -> course not added to output, but added to cycle
        # unvisited -> course has not been added to output or cycle
        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle: 
                return False
            if crs in visit:
                return True

            cycle.add(crs) # this means we are visiting the course rn 
            for pre in prereq[crs]:
                if dfs(pre) == False: # if a course's prereq is itself(it leads to a cycle) means the course schedule is impossible hence False
                    return False
            cycle.remove(crs)
            visit.add(crs) # this mean we are done visiting the course
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
