class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                return mid

            # Right sorted portion of the array
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            # Left sorted portion of the array
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid
                else:
                    r = mid - 1
                         
        return -1
        