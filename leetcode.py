from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)

        for i in strs:
            sorted_word = "".join(sorted(i))
            myDict[sorted_word].append(i)
        
        return list(myDict.values())