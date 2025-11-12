class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxarea = 0
        visited = set()

        def dfs(i, j):
            if i not in range(m) or j not in range(n) or (i, j) in visited or grid[i][j] == 0:
                return 0
            visited.add((i, j))
            return 1 + dfs(i-1, j) + dfs(i, j-1) + dfs(i+1, j) + dfs(i, j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxarea = max(dfs(i, j), maxarea)
        
        return maxarea
