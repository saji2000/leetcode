class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackIndex = stack.pop()[1]
                ans[stackIndex] = (i - stackIndex)
            stack.append([t, i])
        return ans