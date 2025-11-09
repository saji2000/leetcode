class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0

        counts = {}
        longest = 0
        max_count = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_count = max(counts.values())

            while (r - l + 1) - max_count > k:
                counts[s[l]] -= 1
                l += 1

            longest = max(longest, (r - l + 1))
        return longest