class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        my_dict = dict()

        if len(pattern) != len(s):
            return False
        if len(set(pattern)) != len(set(s)):
            return False

        for i in range(len(s)):
            if pattern[i] in my_dict:
                if s[i] != my_dict.get(pattern[i]):
                    return False
            else:
                my_dict[pattern[i]] = s[i]
        return True
