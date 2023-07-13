import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(val for val in s if val.isalnum().lower())
        return s == s[::-1]


solution = Solution()

solution.isPalindrome("here")
