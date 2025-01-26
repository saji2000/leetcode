class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary_s = {}
        dictionary_t = {}
        for i in s:
            if i not in dictionary_s:
                dictionary_s[i] = 1
            else:
                dictionary_s[i] += 1
        dictionary_t = {}
        for i in t:
            if i not in dictionary_t:
                dictionary_t[i] = 1
            else:
                dictionary_t[i] += 1
        return dictionary_t == dictionary_s