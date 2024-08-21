class Solution:
    def search(self, nums, target) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print("l: " + str(l))
            print("r: " + str(r))
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


solution = Solution()
print(solution.search([0, 1, 5, 7, 9, 12], 12))