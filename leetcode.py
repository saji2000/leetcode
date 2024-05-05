class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxArea