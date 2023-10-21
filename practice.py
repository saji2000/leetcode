class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return
        ans = []

        l = 0
        r = 0

        while r < len(nums):
            if nums[r] != nums[r + 1] - 1:
                if l == r:
                    ans.append(str(nums[r]))
                else:
                    ans.append(str(nums[l]) + "->" + str(nums[r]))
                    l = r + 1
            r += 1

        if l == r:
            ans.append(str(nums[l]))
        else:
            ans.append(str(nums[l]) + "->" + str(nums[r]))

        return ans
