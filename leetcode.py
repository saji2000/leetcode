class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLength = 0
        while r <= len(s) - 1:
            while s[r] in s[l:r]:
                l += 1
            maxLength = max(maxLength, len(s[l:r + 1]))
            r += 1
        return maxLength