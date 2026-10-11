class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        def dfs(r, c, prev, visited):
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or heights[r][c] < prev:
                return
            visited.add((r, c))
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)

        pac = set()
        atl = set()
        for r in range(ROWS):
            dfs(r, 0, -1, pac)
            dfs(r, COLS - 1, -1, atl)

        for c in range(COLS):
            dfs(0, c, -1, pac)
            dfs(ROWS - 1, c, -1, atl)

        return list(pac & atl)
            