class Solution:
    def maxArea(self, height: List[int]) -> int:
        # find pair such that min(left, right) * (right - left) is max
        start, end = 0, len(height) - 1
        max_area = float('-inf')
        while start < end:
            area = min(height[start], height[end]) * (end - start)
            max_area = max(max_area, area)
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return max_area



