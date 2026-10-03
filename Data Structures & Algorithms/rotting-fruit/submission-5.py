class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        fresh = 0

        visited = defaultdict(int)

        def bfs(r, c):
            nonlocal fresh
            if min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]) or (r, c) in visited or grid[r][c] == 0:
                return False
            visited[(r, c)] = 1
            if grid[r][c] == 1:
                fresh -= 1
                grid[r][c] = 2
            q.append([r + 1, c])
            q.append([r - 1, c])
            q.append([r, c + 1])
            q.append([r, c - 1])
            return True

        timer = -1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        while q and fresh != 0:
            for i in range(len(q)):
                r, c = q.popleft()
                bfs(r, c)

            timer += 1
        
        return -1 if fresh != 0 else max(timer, 0)