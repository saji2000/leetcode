class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums) < 2):
            return
        i = 0
        j = 0
        while i < len(nums):
            if(nums[i] != 0):
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                j += 1
            i += 1
                