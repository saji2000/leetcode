class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0

        memo = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        for i in reversed(range(0, len(s))):
            if (i < len(s) - 1) and (
                s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M")
            ):
                sum -= 100

            elif (i < len(s) - 1) and (
                s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C")
            ):
                sum -= 10

            elif (i < len(s) - 1) and (
                s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X")
            ):
                sum -= 1

            else:
                sum += memo[s[i]]

        return sum


solution = Solution()

print(solution.romanToInt("MCMXCIV"))
