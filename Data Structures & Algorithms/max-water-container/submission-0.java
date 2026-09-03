class Solution {
    public int maxArea(int[] heights) {
        int max = 0;
        for (int i = 0; i < heights.length; i++) {
            int j = heights.length - 1;

            while (j > i) {
                int volume = Math.min(heights[i], heights[j]) * (j - i);
                if (volume > max) {
                    max = volume;
                }
                j--;
            }
        }
        return max;
    }
}
