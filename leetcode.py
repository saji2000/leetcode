class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max_length = 0

        for i in my_set:
            if (i - 1) not in my_set:
                length = 1
                while i + length in my_set:
                    length += 1
                max_length = max(max_length, length)
        return max_length