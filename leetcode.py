class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            remainder = n % 2
            n = n // 2
            if remainder:
                count += 1
        return count
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(len(ans)):
            ans[i] = self.hammingWeight(i)
        return ans
        