class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_n = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                min_n = min(nums[l], min_n)
                return min_n

            mid = (l + r) // 2
            min_n = min(min_n, nums[mid])       
             
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return min_n