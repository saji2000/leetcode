class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(i, j, k):
            if k == len(word):
                return True
            
            if i < 0 or j < 0 or i >= len(board[0]) or j >= len(board) or board[j][i] != word[k]:
                return False
            
            temp = board[j][i]
            board[j][i] = ''
            if backtrack(i + 1, j, k + 1) or backtrack(i - 1, j, k + 1) or backtrack(i, j + 1, k + 1) or backtrack(i, j - 1, k + 1):
                return True
            board[j][i] = temp
            return False
        

        for j in range(len(board)):
            for i in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False