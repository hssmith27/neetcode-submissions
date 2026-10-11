class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        def explore(r, c):
            q.append([r + 1, c])
            q.append([r - 1, c])
            q.append([r, c + 1])
            q.append([r, c - 1])
        visited = {}
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    explore(r, c)
                    visited[(r, c)] = 1

        level = 1
        

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == -1 or (r, c) in visited:
                    continue
                else:
                    visited[(r, c)] = 1
                    grid[r][c] = level
                    explore(r, c)

            level += 1