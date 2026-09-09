class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        def addGrid(r, c):
            q.append((r+1, c))
            q.append((r-1, c))
            q.append((r, c+1))
            q.append((r, c-1))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == -1 or (r, c) in visited:
                    continue
                visited.add((r, c))
                grid[r][c] = dist
                addGrid(r, c)

            dist += 1
