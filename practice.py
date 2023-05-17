class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        expected = sorted(heights)
        num = 0

        for i in range(len(heights)):
            if(heights[i] != expected[i]):
                num += 1
        
        return num