class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(k, l):
            grid[k][l] = 0

            for dr, dc in directions:
                nr, nc = k+dr, l+dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                    dfs(nr, nc)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count 
