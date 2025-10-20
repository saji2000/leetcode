class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max_length = 0

        for i in my_set:
            if i - 1 not in my_set:
                length = 1
                j = i
                while j + 1 in my_set:
                    j += 1
                    length += 1
                max_length = max(max_length, length)
        return max_length