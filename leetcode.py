class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        sub = set()
        l = 0
        for i in range(len(s)):
            while s[i] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[i])
            length = max(length, len(sub))
        return length
