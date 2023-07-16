class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        sorted_nums = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        return sorted_nums[:k]


solution = Solution()

solution.topKFrequent([[1, 1, 1, 2, 2, 3]])
