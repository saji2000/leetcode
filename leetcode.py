class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxLength = 0
        myDict = {}

        while r < len(s):
            if s[r] not in myDict:
                myDict[s[r]] = 1
            else:
                myDict[s[r]] += 1
            values = myDict.values()
            while (sum(values) - max(values)) > k:
                myDict[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, len(s[l:r + 1]))
            r += 1
        return maxLength
        

        