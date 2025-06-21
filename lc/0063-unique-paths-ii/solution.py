class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # n = len(obstacleGrid)
        # m = len(obstacleGrid[0])
        # memo = [[0]*m for i in range(n)]
        # direction = [
        #     [0, 1],
        #     [1, 0],
        #     [0, -1],
        #     [-1, 0],
        # ]
        # result = 0
        # seen = set()
        
        # def h(i, j):
        #     ...

        # for i in range(m):
        #     for j in range(n):
        #         if obstacleGrid[i][j] == 0 and (i, j) not in seen:
        #             h(i, j)
        
        # return result
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols
        dp[0] = 1

        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                else:
                    if c > 0:
                        dp[c] += dp[c-1]
        
        return dp[cols - 1]
