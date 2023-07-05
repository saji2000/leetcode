class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0

        memo = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        for i in range(0, len(s)):
            if i < (len(s) - 1) and memo[s[i]] < memo[s[i + 1]]:
                sum -= memo[s[i]]
            else:
                sum += memo[s[i]]

        return sum


solution = Solution()

print(solution.romanToInt("MCMXCIV"))
