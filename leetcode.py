class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        i = 0

        while i < len(temperatures) - 1:
            
            j = i + 1

            while j < len(temperatures) and temperatures[i] >= temperatures[j]:
                j += 1

            if j != len(temperatures):
                res[i] = (j - i)

            i += 1

        return res