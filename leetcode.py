class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows - 1
        row = -1
        while l <= r:
            mid = (l + r) // 2

            row_start = matrix[mid][0]
            row_end = matrix[mid][cols - 1]

            if target < row_start:
                r = mid - 1
            
            elif target > row_end:
                l = mid + 1
            
            else:
                row = mid
                break

        if row == -1:
            return False

        l, r = 0, cols - 1


        while l <= r:
            mid = (l + r) // 2
            num = matrix[row][mid]

            if num > target:
                r = mid - 1     
                       
            elif num < target:
                l = mid + 1

            else:
                return True
        
        return False




