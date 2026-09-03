class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        cols = len(matrix[0])
        l = 0
        r = len(matrix) * cols - 1

        while l <= r:
            m = (r - l) // 2 + l
            pair = self.numToPair(m, cols)
            mv = matrix[pair[0]][pair[1]]
            if mv == target:
                return True
            elif mv < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
            
    def numToPair(self, num, cols):
        return [num // cols, num % cols]