#Binary Search solution
class Solution:
    def search(self, nums, target) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1
solution = Solution()
print(solution.search([0, 1, 5, 7, 9, 12], 9))