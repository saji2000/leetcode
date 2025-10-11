from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)

        ordered = sorted(freqs.items(), key = lambda x: x[1], reverse=True)

        top_k = []

        for i in ordered:
            top_k.append(i[0])
        
        return top_k[0:k]