class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * (min(heights[l], heights[r]))
            
            maxArea = max(area, maxArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea