class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


solution = Solution()

solution.strStr("mississippi", "issip")
