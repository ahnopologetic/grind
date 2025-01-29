from collections import deque 
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # solve this in bfs
        rows, cols = len(mat), len(mat[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = 999999
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if mat[new_row][new_col] > mat[row][col]:
                        mat[new_row][new_col] = mat[row][col] + 1
                        queue.append((new_row, new_col))
        
        return mat

