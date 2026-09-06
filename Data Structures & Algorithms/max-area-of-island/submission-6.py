class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        newGrid = grid.copy()

        def totalIsland(r, c):
            if r < 0 or c < 0 or r >= len(newGrid) or c >= len(newGrid[0]):
                return 0
            elif newGrid[r][c] == 0:
                return 0
            newGrid[r][c] = 0
            up = totalIsland(r - 1, c)
            down = totalIsland(r + 1, c)
            left = totalIsland(r, c - 1)
            right = totalIsland(r, c + 1)

            return 1 + up + down + left + right
        
        for i in range(len(newGrid)):
            for j in range(len(newGrid[0])):
                if newGrid[i][j] == 1:
                    res = max(res, totalIsland(i, j))

        return res