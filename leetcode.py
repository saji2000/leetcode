class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for i in strs:
            myDict[''.join(sorted(i))].append(i)
        return myDict.values()