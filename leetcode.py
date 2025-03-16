class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r)//2
            num = matrix[mid][0]
            if matrix[mid][0] < target and matrix[mid][-1] > target:
                break
            elif num > target:
                r = mid - 1
            elif num < target:
                l = mid + 1
            else:
                return True

        index = (l + r) // 2
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = (l + r)//2
            num = matrix[index][mid]
            if num > target:
                r = mid - 1
            elif num < target:
                l = mid + 1
            else:
                return True
        return False