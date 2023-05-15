class Solution:
    def sortArrayByParity(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums) < 2):
            return nums
        i = 0
        j = 0
        while i < len(nums):
            if(nums[i]%2 == 0):
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                j += 1
            i += 1
        return nums