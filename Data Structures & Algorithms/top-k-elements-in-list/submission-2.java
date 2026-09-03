class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i]) + 1);
            }
            else {
                map.put(nums[i], 1);
            }
        }

        int[] frequency = new int[k];
        int topKey = -1001;

        for (int j = 0; j < k; j++) {
            for (Integer key : map.keySet()) {
                if (topKey == -1001 || map.get(key) > map.get(topKey)) {
                    topKey = key;
                }
            }
            frequency[j] = topKey;
            map.remove(topKey);
            topKey = -1001;
        }

        return frequency;
    }
}
