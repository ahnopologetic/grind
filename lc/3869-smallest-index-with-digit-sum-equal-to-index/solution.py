class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum_digits(num):
            res = 0
            while num:
                num, remainder = divmod(num, 10)
                res += remainder
            return res

        for i in range(len(nums)):
            # sum of the digits => 10 => 1, 0 => 1+0 => 1
            if i == sum_digits(nums[i]):
                return i
        return -1
