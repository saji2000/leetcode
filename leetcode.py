class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}

        for i in nums:
            if i not in myDict:
                myDict[i] = 1
            else:
                myDict[i] += 1
        freq = sorted(myDict.items(), key = lambda x: x[1], reverse=True)
        top_k = []
        for i in freq[:k]:
            top_k.append(i[0])
        return top_k
        