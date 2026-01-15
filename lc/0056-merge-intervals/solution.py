class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        res = [intervals[0]]

        for interval in intervals:
            if interval[0] <= res[-1][1] <= interval[1]:
                res[-1][1] = interval[1]
            elif res[-1][0] <= interval[0] and res[-1][1] >= interval[1]:
                continue
            else:
                res.append(interval)
        
        return res

