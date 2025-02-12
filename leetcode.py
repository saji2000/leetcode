class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        maxLength = 0

        for n in mySet:
            if n - 1 not in mySet:
                length = 1
                while n + 1 in mySet:
                    length += 1
                    n += 1
                maxLength = max(maxLength, length)
        
        return maxLength