class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        visited = {}

        def bfs(r, c):
            if min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0 or (r, c) in visited:
                return 0
            res = 0
            if grid[r][c] == 1:
                res = 1
                grid[r][c] = 2
            visited[(r, c)] = 1
            q.append([r + 1, c])
            q.append([r - 1, c])
            q.append([r, c + 1])
            q.append([r, c - 1])
            return res
             

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    bfs(i, j)

        timer = 0

        while q and fresh != 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                fresh -= bfs(r, c)

            timer += 1

        return timer if fresh == 0 else -1