class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Boolean> vals = new HashMap<>();
        for (int num : nums) {
            if (vals.containsKey(num)) {
                return true;
            }
            vals.put(num, true);
        }
        return false;
    }
}