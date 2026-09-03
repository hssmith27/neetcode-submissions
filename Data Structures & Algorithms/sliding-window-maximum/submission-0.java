class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] res = new int[nums.length - k + 1];
        for (int r = 0; r < nums.length - k + 1; r++) {
            int max = nums[r];
            for (int s = r + 1; s < r + k; s++) {
                if (nums[s] > max) {
                    max = nums[s];
                }   
            }
            res[r] = max;
        }
        return res;
    }
}
