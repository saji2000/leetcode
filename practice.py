class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return nums[0]
        
        memo = {}
        
        for num in nums:
            if num in memo:
                memo[num] += 1
            else:
                memo[num] = 1
            
        max = 1
        ans = 0
        for num in memo:
            if memo[num] > max:
                max = memo[num]
                ans = num
        
        return ans

