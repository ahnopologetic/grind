from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs + increment number
        m = len(grid)
        n = len(grid[0])
        result = 0
        q = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        directions = (0, 1), (1, 0), (0, -1), (-1, 0)
        while q and fresh > 0:
            for _ in range(len(q)):
                (r, c) = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            result += 1
        return result if fresh == 0 else -1

