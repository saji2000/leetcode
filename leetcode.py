class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(used, cur):
            if len(cur) == len(nums):
                result.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    cur.append(nums[i])
                    backtrack(used, cur)
                    cur.pop()
                    used[i] = False
        
        backtrack([False] * len(nums), [])
        return result
        