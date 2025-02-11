class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        maxLength = 0
        for i in nums:
            if i - 1 not in mySet:
                ptr = i
                length = 1
                while ptr + 1 in mySet:
                    length += 1
                    ptr += 1
                maxLength = max(maxLength, length)
        return maxLength
        