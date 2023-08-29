class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = 1
        length = 1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                length += 1
            elif nums[i] == nums[i + 1]:
                continue
            else:
                length = 1
            if length > longest:
                longest = length
        return longest
