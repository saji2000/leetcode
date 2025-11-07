class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        my_set = set()

        while l < len(s):
            if r == len(s) or s[r] in my_set:
                my_set.clear()
                l += 1
                r = l
            else:
                my_set.add(s[r])
                longest = max(longest, len(my_set))
                r += 1
        return longest
            
        