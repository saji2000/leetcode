class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        if(len(nums) < 2):
            return nums[0]
        
        max_list = [] 
        nums.sort()
        max = nums[0]
        ans = 0

        for i in range(len(nums)):
            if(nums[i] >= max and ans < 3):
                max = nums[i]
                max_list.append(max)
                ans += 1

        if(len(max_list) < 3):
            return max_list[-1]
        
        return max_list[0]