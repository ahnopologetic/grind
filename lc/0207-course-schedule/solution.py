class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs or bfs question
        adj_list = self.build_adj_list(numCourses, prerequisites)

        state = [0] * numCourses

        def has_cycle(v):
            if state[v] == 1:
                # This vertex is processed so we pass.
                return False
            if state[v] == -1:
                # This vertex is being processed and it means we have a cycle.
                return True

            # Set state to -1
            state[v] = -1

            for i in adj_list[v]:
                if has_cycle(i):
                    return True

            state[v] = 1
            return False
        for v in range(numCourses):
            if has_cycle(v):
                return False
    
        return True
    
    def build_adj_list(self, n, edgesList):
        adj_list = [[] for _ in range(n)]
        for c1, c2 in edgesList:
            adj_list[c2].append(c1)
        return adj_list
        
