class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = Counter(nums)
        
        values = sorted(myDict.keys(), key = lambda i: myDict[i], reverse=True)

        return values[:k]
