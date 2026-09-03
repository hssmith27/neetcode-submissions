class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def countLand(i, j):
            if ((i >= len(grid) or i < 0) or (j >= len(grid[0]) or j < 0)) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + countLand(i + 1, j) + countLand(i - 1, j) + countLand(i, j + 1) + countLand(i, j - 1)
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, countLand(i, j))

        return res