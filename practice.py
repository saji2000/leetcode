class Solution:
    def sortArrayByParity(self, nums: List[int]) -> None:
        # here
        if(len(nums) < 2):
            return nums
        odd = []
        even = []
        i = 0
        while i < len(nums):
            if(nums[i]%2 == 0):
                even.append(nums[i])
            else:
                odd.append(nums[i])
            i += 1

        return (even + odd)