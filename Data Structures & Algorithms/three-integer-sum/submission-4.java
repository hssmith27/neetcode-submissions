class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();

        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            int target = nums[i] * (-1);
            int left = i + 1;
            int right = nums.length - 1;

            while (right > left) {
                if (nums[right] + nums[left] == target) {
                    ArrayList<Integer> triplet = new ArrayList<>();
                    triplet.add(nums[i]);
                    triplet.add(nums[left]);
                    triplet.add(nums[right]);
                    
                    if (!res.contains(triplet)) {
                        res.add(triplet);
                    }
                    left++;
                }
                else if (nums[right] + nums[left] > target) {
                    right--;
                }
                else {
                    left++;
                }
            }
        }

        return res;
    }
}
