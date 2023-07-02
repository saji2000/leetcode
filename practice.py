class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 0
        length = len(nums)

        for i in range(0, length - 2):
            if nums[i] == nums[i + 2]:
                j = i + 2
                start = j
                while j < length - 2 and nums[i] == nums[j]:
                    j += 1
                    k += 1
                nums[start:j] = nums[j:]
        return length - k 