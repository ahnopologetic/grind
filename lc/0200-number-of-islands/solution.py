class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        count = 0
        def dfs(m, n):
            grid[m][n] = 0
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                r = m + dr
                c = n + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
                    dfs(r, c)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
