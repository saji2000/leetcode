class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        prefixProduct = 1

        for i in range(n):
            result[i] *= prefixProduct
            prefixProduct *= nums[i]
        
        suffixProduct = 1

        for i in reversed(range(n)):
            result[i] *= suffixProduct
            suffixProduct *= nums[i]
        
        return result