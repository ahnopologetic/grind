from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # how this can be a queue problem?
        # RD -> R - ban, D - x, queue is empty
        r = deque()
        d = deque()
        n = len(senate)

        for idx, s in enumerate(senate):
            if s == "R":
                r.append(idx)
            else:
                d.append(idx)
        
        while r and d:
            rs, ds = r.popleft(), d.popleft()
            if rs < ds:
                r.append(rs+n)
            else:
                d.append(ds+n)
        
        return "Radiant" if r else "Dire"

