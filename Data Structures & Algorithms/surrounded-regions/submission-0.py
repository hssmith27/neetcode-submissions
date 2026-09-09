class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        reached = set()
        q = deque()

        def explore(r, c):
            q.append((r+1, c))
            q.append((r-1, c))
            q.append((r, c+1))
            q.append((r, c-1))

        for i in range(COLS):
            if board[0][i] == "O":
                q.append((0, i))
            if board[ROWS - 1][i] == "O":
                q.append((ROWS - 1, i))

        for i in range(ROWS):
            if board[i][0] == "O":
                q.append((i, 0))
            if board[i][COLS - 1] == "O":
                q.append((i, COLS - 1))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in reached or board[r][c] == "X":
                    continue
                reached.add((r, c))
                explore(r, c)

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in reached:
                    board[i][j] = "X"

        