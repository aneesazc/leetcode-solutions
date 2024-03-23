class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list to represent the graph of course dependencies
        adj = {i:[] for i in range(numCourses)}
        for src, dst in prerequisites:
            adj[src].append(dst)  # Add a directed edge from src to dst in the graph

        # Sets to keep track of visited and currently visiting nodes (courses) during DFS
        visit = set()     # Set of all courses that have been completely explored
        visiting = set()  # Set of courses currently being explored

        # Depth-first search function to detect cycles in the graph
        def dfs(course):
            if course in visit:  # If the course has already been explored, no need to explore again
                return True
            if course in visiting:  # If the course is currently being explored, a cycle is detected
                return False
            
            visiting.add(course)  # Mark the course as currently being explored

            # Explore all prerequisites (next courses) for the current course
            for nextC in adj[course]:
                if not dfs(nextC):  # If a cycle is found in any prerequisite course, return False
                    return False

            # Once all prerequisites are explored, move the course from 'visiting' to 'visit'
            visiting.remove(course)
            visit.add(course)
            return True  # No cycles detected for this course

        # Iterate through all courses and apply DFS to detect cycles
        for i in range(numCourses):
            if not dfs(i):  # If a cycle is detected for any course, the schedule is impossible
                return False
        
        return True  # No cycles detected; all courses can be completed
