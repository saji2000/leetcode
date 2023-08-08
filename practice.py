class Solution:
    memo = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if (n - 1) in self.memo:
            num_1 = self.memo[n - 1]
        else:
            self.memo[n - 1] = self.climbStairs(n - 1)
            num_1 = self.memo[n - 1]
        if (n - 2) in self.memo:
            num_2 = self.memo[n - 2]
        else:
            self.memo[n - 2] = self.climbStairs(n - 2)
            num_2 = self.memo[n - 2]

        return num_1 + num_2
