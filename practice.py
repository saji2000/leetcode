class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()

        return len(arr[-1])


solution = Solution()

print(solution.lengthOfLastWord("MCMXCIV"))
