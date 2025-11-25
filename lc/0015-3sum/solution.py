class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort -> n * two pointer search
        # we can reduce n if curr is more than or equal 1 -> it will always be increasing
        # O(n^2) -> still better than O(n^3)
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            curr = nums[i]
            complement = -curr
            start, end = i + 1, len(nums) - 1
            while start < end:
                pair_sum = nums[start] + nums[end]
                if pair_sum == complement:
                    result.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                elif pair_sum < complement:
                    start += 1
                else: 
                    end -= 1
        return list(result)
