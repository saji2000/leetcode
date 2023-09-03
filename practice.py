class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return 0

        ans = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while r > l and nums[r] == nums[r - 1]:
                        r -= 1
                    while l > l and nums[l] == nums[l + 1]:
                        l += 1

        return ans
