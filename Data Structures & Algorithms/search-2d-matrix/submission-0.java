class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (i + 1 < matrix.length && target >= matrix[i + 1][0]) {
                    continue;
                }
                if (matrix[i][j] == target) {
                    return true;
                }
            }
        }
        return false;
    }
}
