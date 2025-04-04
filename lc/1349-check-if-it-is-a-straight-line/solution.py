class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        [[x1, y1], [x2, y2]] = coordinates[:2]
        gradient = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else 0
        prev = (x1, y1)
        for [x, y] in coordinates[2:]:
            try:
                curr_gradient = (y - prev[1]) / (x - prev[0])
            except ZeroDivisionError:
                curr_gradient = 0
            
            if x1 == x2 == 0 and x != 0:
                return False
            if y1 == y2 == 0 and y != 0:
                return False

            if curr_gradient != gradient:
                return False
        
        return True
            

