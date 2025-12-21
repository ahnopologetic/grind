class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack: O(n^2) -> O(n)
        res = [0] * len(temperatures)
        stack = [] # (temp, idx)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t, i = stack.pop()
                res[i] = idx - i
            stack.append((temp, idx))
        return res
            
