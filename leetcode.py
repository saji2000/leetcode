class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for i in nums:
            if i not in myDict:
                myDict[i] = 1
            else:
                myDict[i] += 1
        return sorted(myDict.keys(), key = lambda i: myDict[i], reverse=True)[:k]