class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        num_of_lands = 0
        
        def bfs(row, col):
            q = deque()
            
            visited.add((row, col))
            q.append((row, col))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    # val = grid[row+r][col+c]
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    num_of_lands += 1
                    bfs(row, col)
        
        return num_of_lands
