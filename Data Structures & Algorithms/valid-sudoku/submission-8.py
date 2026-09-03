class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                val = board[r][c]
                if val != ".":
                    box_idx = (r // 3, c // 3)
                    if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                        return False
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)

        return True
        