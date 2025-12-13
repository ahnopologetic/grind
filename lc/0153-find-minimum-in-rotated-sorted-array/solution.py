class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log n) -> use binary search
        # find minimum
        # binary search modified
        # look for lower

        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
                
