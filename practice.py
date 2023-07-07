class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min = 10000000
        min_word = None
        for i in range(0, len(strs)):
            if len(strs[i]) < min:
                min = len(strs[i])
                min_word = strs[i]

        new_str = min_word
        for i in strs:
            for j in reversed(range(0, len(min_word))):
                if min_word[j] != i[j]:
                    new_str = new_str[:j]

        return new_str


solution = Solution()

print(solution.longestCommonPrefix("MCMXCIV"))
