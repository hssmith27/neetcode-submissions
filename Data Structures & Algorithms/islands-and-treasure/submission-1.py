class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        def expand(r, c):
            q.append([r + 1, c])
            q.append([r - 1, c])
            q.append([r, c + 1])
            q.append([r, c - 1])

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    expand(i, j)

        dist = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 2147483647:
                    continue
                grid[r][c] = dist
                expand(r, c)

            dist += 1