class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # two pointer
        result = set()
        nums.sort()
        n = len(nums)

        for i in range(n - 3):
            # add unique combination
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j + 1, n - 1

                while l < r:
                    four_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if four_sum < target:
                        l += 1
                    elif four_sum > target:
                        r -= 1
                    else:
                        result.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r-= 1


        return [list(pair) for pair in result]
