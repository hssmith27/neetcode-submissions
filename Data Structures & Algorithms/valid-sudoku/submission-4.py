class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}
        nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for i in range(len(board)):
            rows[i] = []
            cols[i] = []
            squares[i] = []

        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]
                if val != ".":
                    # check rows
                    if val in rows[i] or val not in nums:
                        return False
                    rows[i] = rows[i] + [val]

                    # check cols
                    if val in cols[j] or val not in nums:
                        return False
                    cols[j] = cols[j] + [val]

                    # check squares
                    square_num = (3 * int(i / 3)) + (int(j / 3))
                    if val in squares[square_num] or val not in nums:
                        return False
                    squares[square_num] = squares[square_num] + [val]

        return True
