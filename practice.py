class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        numbers = set(nums)

        ans = []

        for i in range(1, len(nums) + 1):
            if(i  not in numbers):
                ans.append(i)
        
        return ans