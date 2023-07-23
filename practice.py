class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        ans = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        return ans[0:k]
