class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = dict()
        ans = []
        for i in range(len(strs)):
            myStr = strs[i]
            myStr = ''.join(sorted(myStr))
            if myStr not in myDict:
                myDict[myStr] = []
            myDict[myStr].append(strs[i])
        for i in myDict.values():
            ans.append(i)
        return ans
