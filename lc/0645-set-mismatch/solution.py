class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # counter + 1 upto len(nums) = n
        # for num in nums, decrement by one of the counter
        # return numbers that are not zero.

        n = len(nums)
        c = Counter([i for i in range(1, n + 1)])
        twice = 0
        for num in nums:
            c[num] -= 1
            if c[num] == -1:
                twice = num
        
        missing = next(k for k, v in c.items() if v == 1)
        
        return [twice, missing]

