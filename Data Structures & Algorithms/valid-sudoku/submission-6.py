class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]
                if val != ".":
                    if val in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        if val in rows[i] or val in cols[j] or val in boxes[(i // 3, j // 3)]:
                            return False
                        else:
                            rows[i].add(val)
                            cols[j].add(val)
                            boxes[(i // 3, j // 3)].add(val)
                    else:
                        return False


        return True
