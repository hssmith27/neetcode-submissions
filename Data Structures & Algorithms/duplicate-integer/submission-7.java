class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Boolean> vals = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (vals.containsKey(nums[i])) {
                return true;
            }
            vals.put(nums[i], true);
        }
        return false;
    }
}