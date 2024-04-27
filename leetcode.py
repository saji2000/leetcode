class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = dict()

        for i in nums:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1
        
        values = sorted(myDict.keys(), key = lambda i: myDict[i], reverse=True)

        return values[:k]
