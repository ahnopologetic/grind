class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        # BF: dict for duplicate check O(n), list for adj nums O(n^2)
        # better: dict filled with nums, list for adj candidates (can overlap)

        d = {}
        res = [] # lonely

        for num in nums:
            if d.get(num): # duplicate
                d[num] += 1
                continue
            d[num] = 1
        print(f"{d=}")
        
        for k, v in d.items():
            if v > 1:
                continue
            if not d.get(k-1) and not d.get(k+1):
                res.append(k)

        return res

