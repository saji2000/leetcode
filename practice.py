class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Initialize output array
        result = [1] * n

        # Compute left products
        left_product = 1
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]
            print("Left Product: ", left_product)
            print("Left: ", result)

        # Compute right products and combine with left products
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
            print("Right Product: ", right_product)
            print("Right: ", result)

        return result


nums = [1, 2, 3, 4]
solution = Solution()
output = solution.productExceptSelf(nums)
print(output)  # Output: [24, 12, 8, 6]
