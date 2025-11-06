class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute-force
        # result = []
        # curr = 0

        # for i in range(len(nums)):
        #     for j in range(curr + 1, len(nums)):
        #         if nums[curr] + nums[j] == target:
        #             result = [curr, j]
        #     curr += 1

        # return result

        # two-pass hash table
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        
        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in d and d[complement] != j:
                return [j, d[complement]]
        
        return []
