class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        i = 0
        while i < len(nums):
            print(nums[i])
            if(nums[i] == val):
                del nums[i]
                nums.append(0)
                k += 1
                i -= 1
            i += 1
        return len(nums) - k
