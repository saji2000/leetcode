class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        numbers = set(nums)
        
        if(len(numbers) < 3):
            return max(numbers)
        
        numbers.remove(max(numbers))
        numbers.remove(max(numbers))

        return max(numbers)