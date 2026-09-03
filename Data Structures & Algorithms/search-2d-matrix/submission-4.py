class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (r + l) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                break

        if not (l <= r):
            return False
        row = (l + r) // 2
        f, s = 0, len(matrix[row]) - 1
        while f <= s:
            m = (f + s) // 2
            if matrix[row][m] > target:
                s = m - 1
            elif matrix[row][m] < target:
                f = m + 1
            else:
                return True
        
        return False