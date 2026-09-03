class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        int product = 1;
        boolean hasZero = false;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                if (hasZero) {
                    product = 0;
                }
                hasZero = true;
            }
            else {
                product *= nums[i];
            }
        }

        for (int i = 0; i < nums.length; i++) {
            if (hasZero) {
                if (nums[i] != 0) {
                    res[i] = 0;
                }
                else {
                    res[i] = product;
                }
            }
            else {
                res[i] = product / nums[i];
            }
        }

        return res;
    }
}  
