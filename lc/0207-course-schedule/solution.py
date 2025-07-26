class Solution:
    def buildAdjacencyList(self, n, edgesList):
        adjList = [[] for _ in range(n)]
        # c2 (course 2) is a prerequisite of c1 (course 1)
        # i.e c2c1 is a directed edge in the graph
        for c1, c2 in edgesList:
            adjList[c2].append(c1)
        return adjList


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = self.buildAdjacencyList(numCourses, prerequisites)

        state = [0] * numCourses
        visited = set()

        def has_cycle(v, stack):
            if v in visited:
                if v in stack:
                    return True
                return False
            
            visited.add(v)
            stack.append(v)

            for i in adj_list[v]:
                if has_cycle(i, stack):
                    return True
            
            stack.pop()
            return False
        
        for v in range(numCourses):
            if has_cycle(v, []):
                return False
        
        return True
