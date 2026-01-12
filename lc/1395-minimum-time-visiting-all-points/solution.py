class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # diff = (x_i, y_i) -> (5, 8) => lowest + (highest - lowest) = steps
        # res = increment steps as it goes
        res = 0
        curr = points[0]

        for x, y in points[1:]:
            curr_x, curr_y = curr
            x_i, y_i = abs(x - curr_x), abs(y - curr_y)
            res += min(x_i, y_i) + (max(x_i, y_i) - min(x_i, y_i))
            curr = [x, y]
        
        return res

