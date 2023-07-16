class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        sorted_nums = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        return sorted_nums[:k]


solution = Solution()

solution.topKFrequent([[1, 1, 1, 2, 2, 3]])
