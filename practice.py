class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        max_list = [] 

        max = nums[0]

        nums.sort()

        for i in range(len(nums)):
            if(nums[i] > max):
                max = nums[i]
                max_list.append(max)
        
        print(max_list)
