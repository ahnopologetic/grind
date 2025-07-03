class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # dfs
        # if index other than i (let k) is 1, go there and check if i is 1. 
        # else: count++
        # if nums[i][k] == nums[k][i]: no count
        # else: count++

        def dfs(i: int):
            for j in range(len(isConnected)):
                if not visited[j] and isConnected[i][j]:
                    visited[j] = True
                    dfs(j)
            

        ans = 0
        n = len(isConnected)
        visited = [False] * n


        for i in range(n):
            if not visited[i]:
                ans += 1
                visited[i] = True
                dfs(i)

        return ans
