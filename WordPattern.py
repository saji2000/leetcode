class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(s) != len(pattern):
            return False

        if len(set(s)) != len(set(pattern)):
            return False

        my_dict = {}

        for i in range(len(pattern)):
            if pattern[i] in my_dict:
                if my_dict[pattern[i]] != s[i]:
                    return False
            my_dict[pattern[i]] = s[i]

        return True
