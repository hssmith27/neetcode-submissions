class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxes = defaultdict(list)
        vals = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]
                if val != ".":
                    if val not in vals:
                        return False
                    if val in rows[i]:
                        return False
                    if val in cols[j]:
                        return False
                    box = (i // 3) + (3 * (j // 3))
                    if val in boxes[box]:
                        return False
                    rows[i].append(val)
                    cols[j].append(val)
                    boxes[box].append(val)

        return True