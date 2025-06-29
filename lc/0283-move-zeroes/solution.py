class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zeros = 0
        # i = 0
        # while nums and i < len(nums):
        #     if nums[i] == 0:
        #         zeros += 1
        #         nums.pop(i)
        #     else:
        #         i += 1
        
        # for _ in range(zeros):
        #     nums.append(0)
        # # good enuf, but loop twice

        n = len(nums)
        last = 0

        for i in range(n):
            if nums[i] != 0:
                nums[last], nums[i] = nums[i], nums[last]
                last += 1

        
            



        
