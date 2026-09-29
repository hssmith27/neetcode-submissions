class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def clearIsland(r, c):
            if min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            clearIsland(r + 1, c)
            clearIsland(r - 1, c)
            clearIsland(r, c + 1)
            clearIsland(r, c - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    clearIsland(i, j)

        return res