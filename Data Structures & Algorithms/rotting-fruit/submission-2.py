class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        fresh = 0

        def bfs(r, c):
            nonlocal fresh
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 0:
                return
            if grid[r][c] == 1:
                fresh -= 1
            visited.add((r, c))
            q.append((r + 1, c))
            q.append((r - 1, c))
            q.append((r, c + 1))
            q.append((r, c - 1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    bfs(r, c)
                elif grid[r][c] == 1:
                    fresh += 1

        
        
        time = 0
        while fresh and q:
            for i in range(len(q)):
                r, c = q.popleft()
                bfs(r, c)
            time += 1
                
        return time if fresh == 0 else -1


