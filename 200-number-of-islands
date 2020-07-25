# https://leetcode.com/problems/number-of-islands/
# https://leetcode.com/submissions/detail/371230257/

class Solution:   
    
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0;
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == "1"):
                    num = num + 1
                    self.destroy(grid, i, j)
        return(num)
    
    def destroy(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == "0":
            return
        else:
            grid[x][y] = "0"
            self.destroy(grid, x - 1, y)
            self.destroy(grid, x, y - 1)
            self.destroy(grid, x, y + 1)
            self.destroy(grid, x + 1, y)            
