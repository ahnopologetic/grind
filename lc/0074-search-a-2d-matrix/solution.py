class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # for every row, find i such that target is smaller than row[n-1]
        r = 0
        for i in range(m):
            if matrix[i][n-1] >= target:
                r = i
                break

        # do binary search on the row
        row = matrix[r]
        left, right = 0, n - 1
        while left <= right:
            mid = (right+left) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
