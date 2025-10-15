class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        prev = 1
        for i in range(len(nums)):
            ans[i] = prev
            prev *= nums[i]

        post = 1
        for i in reversed(range(len(nums))):
            ans[i] *= post
            post *= nums[i]

        return ans