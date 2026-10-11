class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        fresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r + 1, c))
                    q.append((r - 1, c))
                    q.append((r, c + 1))
                    q.append((r, c - 1))
        
        timer = 0
        visited = set()

        while q and fresh != 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r, c) in visited:
                    continue
                visited.add((r, c))
                if grid[r][c] == 1:
                    fresh -= 1
                    grid[r][c] = 2
                q.append((r + 1, c))
                q.append((r - 1, c))
                q.append((r, c + 1))
                q.append((r, c - 1))

            timer += 1
                

        return timer if fresh == 0 else -1
