class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        
        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if board[i][j] != word[idx]:
                return False
            letter = board[i][j]
            board[i][j] = "."
            res = dfs(i+1, j, idx + 1) or dfs(i-1, j, idx + 1) or dfs(i, j+1, idx + 1) or dfs(i, j-1, idx + 1)
            board[i][j] = letter
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False