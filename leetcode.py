class Solution:
    def countingBits(self, n: int) -> [int]:
        return str(bin(n)).count('1')