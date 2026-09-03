class Solution {
    public int search(int[] nums, int target) {
        return searchR(nums, target, 0, nums.length - 1);
    }

    public int searchR(int[] nums, int target, int start, int end) {
        if (end - start < 0) {
            return -1;
        }
        int middle = (end - start) / 2 + start;
        if (nums[middle] == target) {
            return middle;
        }
        if (nums[middle] > target) {
            return searchR(nums, target, start, middle - 1);
        }
        else {
            return searchR(nums, target, middle + 1, end);
        }
    }
}
