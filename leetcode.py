class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)

        ordered = sorted(freqs.keys(), key=lambda x: freqs[x], reverse=True)

        return ordered[0:k]