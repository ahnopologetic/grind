from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # dfs
        # count up when 
        # problem: how would you know you're getting closer to 0? 

        def dfs(i: int, min_reorder: list[int]):
            visited[i] = True
            for ngbr, drt in adj[i]:
                if not visited[ngbr]:
                    if drt == 1:
                        min_reorder[0] += 1
                
                    dfs(ngbr, min_reorder)
            return min_reorder

        adj = defaultdict(list)
        visited = [False] * n
        min_reorder = [0]
        
        for connection in connections:
            adj[connection[0]] += [(connection[1], 1)]
            adj[connection[1]] += [(connection[0], -1)]
        result = dfs(0, min_reorder)
        
        return result[0]



