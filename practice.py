class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        ans = []

        memo = {}
        
        def rowColumn(row, column):
            if(column == 0 or row == column):
                return 1
            elif (row, column) in memo:
                return memo[(row, column)]
            else:
                result = rowColumn(row - 1, column - 1) + rowColumn(row - 1, column)
                memo[(row, column)] = result
                return result
            
        
        for i in range(0, rowIndex + 1):
            ans.append(rowColumn(rowIndex, i))

        return ans
        
