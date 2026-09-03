class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i, row, col):
            if i >= len(word):
                return True
            if (row < 0 or col < 0) or (row >= len(board) or col >= len(board[0])):
                return False
            if board[row][col] != word[i]:
                return False
            board[row][col] = "#"
            res = (helper(i + 1, row + 1, col) or 
            helper(i + 1, row - 1, col) or
            helper(i + 1, row, col + 1) or
            helper(i + 1, row, col - 1))
            board[row][col] = word[i]
            return res

        for row in range(len(board)):
            for col in range(len(board[0])):
                if helper(0, row, col):
                    return True
        
        return False
        

