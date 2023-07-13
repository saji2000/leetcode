import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(val for val in s if val.isalnum()).lower()


solution = Solution()

solution.isPalindrome("here")
