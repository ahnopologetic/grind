class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # brute force -> O(n^2logn): sorting + find unique numbers before that
        # brute force 2 -> O(n^2): find 
        # [1, 2, 2, 3, 8]
        # {8: [4], 1: [0], 2: [1, 2], 3: [3]}
        # O(n)

        maps = {}
        for i, num in enumerate(sorted(nums)):
            if num not in maps:
                maps[num] = [i]
            else:
                maps[num] += [maps[num][0]]
        res = []
        for num in nums:
            pos = maps[num][0]
            res += [pos]
            maps[num].pop(0)
        
        return res

