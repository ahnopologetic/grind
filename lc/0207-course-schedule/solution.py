from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # let's implement dfs
        # create a graph first
        pre = defaultdict(list)
        
        for course, req in prerequisites: 
            pre[course].append(req)
        
        taken = set()

        def dfs(course):
            if not pre[course]:
                return True
            
            if course in taken:
                return False
            
            taken.add(course)

            for req in pre[course]:
                if not dfs(req): return False
            
            pre[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        
        return True
        
