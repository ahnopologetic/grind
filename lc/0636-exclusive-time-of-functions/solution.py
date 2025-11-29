class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn, action, ts = log.split(':')
            fn, ts = int(fn), int(ts)

            if action == "start":
                if stack:
                    res[stack[-1][0]] += ts - prev_time
                stack.append((fn, action, ts))
                prev_time = ts
            else:
                pfn, _, _ = stack.pop()
                res[pfn] += (ts - prev_time) + 1
                prev_time = ts + 1
        
        return res
