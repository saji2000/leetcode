class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                return min(minimum, nums[l])

            mid = (l + r) // 2
            minimum = min(minimum, nums[mid])

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return minimum