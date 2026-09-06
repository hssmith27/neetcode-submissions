class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        newGrid = grid.copy()

        def clearIsland(r, c):
            if r < 0 or c < 0 or r >= len(newGrid) or c >= len(newGrid[0]):
                return
            if newGrid[r][c] == "0":
                return
            newGrid[r][c] = "0"
            clearIsland(r + 1, c)
            clearIsland(r - 1, c)
            clearIsland(r, c + 1)
            clearIsland(r, c - 1)

        res = 0
        
        for i in range(len(newGrid)):
            for j in range(len(newGrid[0])):
                if newGrid[i][j] == "1":
                    res += 1
                    clearIsland(i, j)
                
        return res
