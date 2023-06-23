class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        ans = []
        
        def rowColumn(row, column):
            if(column == 0 or row == column):
                return 1
            else:
                return rowColumn(row - 1, column - 1) + rowColumn(row - 1, column)
            
        
        for i in range(0, rowIndex + 1):
            ans.append(rowColumn(rowIndex, i))

        return ans
        
