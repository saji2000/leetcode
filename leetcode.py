class Solution:
    def subsetII(self, nums: List[int]) -> List[List[int]]:
        result = []
        cur = []
        nums.sort()

        def backtrack(index):
            if index == len(nums):
                result.append(cur.copy())
                return
            
            cur.append(nums[index])
            backtrack(index + 1)
            cur.pop()
            
            while index < len(nums) + 1 and nums[index] == nums[index + 1]:
                index += 1
            
            backtrack(index + 1)
        backtrack([])
        return result