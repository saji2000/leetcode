class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        my_set = set()
        string = ""

        while r < len(s):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            
            if s[r] not in my_set:
                my_set.add(s[r])
                longest = max(longest, len(my_set))
                r += 1

        return longest
        