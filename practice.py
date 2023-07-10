class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_t = len(t)
        len_s = len(s)

        if len_t != len_s:
            return False

        memo = {}
        for i in range(0, len_s):
            if s[i] not in memo:
                memo[s[i]] = 1
            else:
                memo[s[i]] += 1

        for i in range(0, len_t):
            if t[i] not in memo:
                return False
            else:
                if memo[t[i]] < 1:
                    return False
                memo[t[i]] -= 1

        return True
