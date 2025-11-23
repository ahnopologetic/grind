from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = defaultdict(list)
        for idx, num in enumerate(nums):
            visited[num] += [idx]
        
        for i, num in enumerate(nums):
            if num in visited:
                if len(visited[num]) == 1:
                    del visited[num]
                else:
                    visited[num].pop(0)
            complement = target - num
            if complement in visited:
                return [i, visited[complement][-1]]
        
        return [0, 1]
