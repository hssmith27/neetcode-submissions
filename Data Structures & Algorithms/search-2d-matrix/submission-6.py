class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            m = (top + bot) // 2
            if matrix[m][0] > target:
                bot = m - 1
            elif matrix[m][-1] < target:
                top = m + 1
            else:
                break
    
        if top > bot:
            return False
        row = (top + bot) // 2
        l, r = 0, len(matrix[row]) - 1
        
        while l <= r:
            col = (r + l) // 2
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = col + 1
            else:
                r = col - 1

        return False