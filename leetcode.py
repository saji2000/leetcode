class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = [1] * n
        pre_product = 1
        for i in range(n):
            product[i] *= pre_product
            pre_product *= nums[i]
        suf_product = 1
        for i in reversed(range(n)):
            product[i] *= suf_product
            suf_product *= nums[i]
        
        return product
