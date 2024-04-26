class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            remainder = n % 2
            n = n//2
            if remainder:
                count += 1
        return count