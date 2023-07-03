class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length  = len(nums)
        k = k % length
        k = length - k

        temp = nums[k:] 
        nums[k:] = nums[0:k]
        nums[0:k] = temp