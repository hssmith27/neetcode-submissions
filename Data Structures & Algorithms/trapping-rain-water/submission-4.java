class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = 1;
        int res = 0;
        
        int[] water = new int[height.length];

        while (left < height.length && right < height.length) {
            if (height[right] < height[left]) {
                water[right] = height[left] - height[right];
                right++;
            }
            else {
                left = right;
                right++;
            }
        }

        left = height.length - 2;
        right = height.length - 1;

        while (left > 0 && right > 0) {
            if (height[right] > height[left]) {
                res += Math.min(water[left], height[right] - height[left]);
                left--;
            }
            else {
                right = left;
                left--;
            }
        }

        return res;
    }
}
