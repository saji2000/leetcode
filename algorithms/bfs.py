# Number of islands using breadth first search
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def bfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                bfs(i, j + 1)
                bfs(i + 1, j)
                bfs(i, j - 1)
                bfs(i - 1, j)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):  
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)
        return count