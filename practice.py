class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while j < len(nums):
            print("j: " + str(j) + " nums[j]:"+ str(nums[j]) + " i: " + str(i) + " nums[i]: " + str(nums[i]))
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i