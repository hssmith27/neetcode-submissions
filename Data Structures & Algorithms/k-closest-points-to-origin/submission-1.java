class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int[][] result = new int[k][2];
        int[] base = new int[2];
        for (int i = 0; i < points.length; i++) {
            int removeIndex = -1;
            for (int j = 0; j < result.length; j++) {
                if (result[j][0] == 0 && result[j][1] == 0) {
                    removeIndex = j;
                    break;
                }
                if (calcDist(points[i]) < calcDist(result[j])) {
                    if (removeIndex == -1
                    || calcDist(result[j]) > calcDist(result[removeIndex])) {
                        removeIndex = j;
                    }                  
                }
            }
            if (removeIndex != -1) {
                result[removeIndex] = points[i];
            }
        }
        return result;
    }

    public double calcDist(int[] point) {
        return Math.sqrt(Math.pow(point[0], 2) + Math.pow(point[1], 2));
    }
}
