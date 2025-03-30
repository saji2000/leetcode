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
            if ((r - l + 1) - max(values)) > k:
                myDict[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r - l + 1)
            r += 1
        return maxLength
        

        