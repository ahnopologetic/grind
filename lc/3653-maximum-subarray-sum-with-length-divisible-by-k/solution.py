class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # Goal: return max sum of subarray whose length is divisible by k
        # get possible multiples of k such that k*m <= len(nums)
        prefSum = 0
        subMax = -sys.maxsize
        minSoFar = [sys.maxsize] * k
        minSoFar[(k - 1) % k] = 0

        for i, v in enumerate(nums):
            prefSum += v
            subMax = max(subMax, prefSum - minSoFar[i % k])
            minSoFar[i % k] = min(minSoFar[i % k], prefSum)

        return subMax
