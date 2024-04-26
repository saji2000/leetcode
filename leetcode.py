class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n

        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return self.memo[n]