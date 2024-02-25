class Solution:
    def countingBits(self, n: int) -> [int]:
        ans = []
        for i in range(0, n + 1):
            count = 0
            while i:
                count += i % 2
                i = i >> 1
            ans.append(count)
        return ans