class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # ans = 0
        # sort interval by start
        # for each interval, check next interval whether it has earlier start than current end, count up when there is until you don't find. 
        ans = 0
        intervals.sort(key=lambda x: x[1])
        last_end = float('-inf')

        for start, end in intervals:
            if last_end > start:
                ans += 1
            else:
                last_end = end
        
        return ans



        
