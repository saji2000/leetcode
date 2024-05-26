class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sub = {}
        l = 0
        length = 0
        for r in range(len(s)):
            if s[r] in sub:
                sub[s[r]] += 1
            else:
                sub[s[r]] = 1

            if (r - l + 1) - max(sub.values()) > k:
                sub[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)
        return length
            