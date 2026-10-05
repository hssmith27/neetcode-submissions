class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()

        def dfs(r, c, prev, ocean, visited):
            if min(r, c) < 0 or r >= len(heights) or c >= len(heights[0]) or (r, c) in visited or prev > heights[r][c]:
                return
            if ocean == "pacific":
                pacific.add((r, c))
            else:
                atlantic.add((r, c))
            visited[(r, c)] = 1
            dfs(r + 1, c, heights[r][c], ocean, visited)
            dfs(r - 1, c, heights[r][c], ocean, visited)
            dfs(r, c + 1, heights[r][c], ocean, visited)
            dfs(r, c - 1, heights[r][c], ocean, visited)

        for i in range(len(heights)):
            visited = {}
            dfs(i, 0, -1, "pacific", visited)
            visited = {}
            dfs(i, len(heights[0]) - 1, -1, "atlantic", visited)

        for i in range(len(heights[0])):
            visited = {}
            dfs(0, i, -1, "pacific", visited)
            visited = {}
            dfs(len(heights) - 1, i, -1, "atlantic", visited)

        return [list(t) for t in atlantic.intersection(pacific)]

        