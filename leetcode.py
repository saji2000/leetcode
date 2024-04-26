class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(len(ans)):
            ans[i] = i.bit_count()
        return ans
        