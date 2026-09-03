class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] res = new int[k];

        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i]) + 1);
            }
            else {
                map.put(nums[i], 1);
            }
        }

        Object[] keys = map.keySet().toArray();

        for (int i = 0; i < k; i++) {
            int max = 0;
            int maxElement = -1001;
            for (int j = 0; j < keys.length; j++) {
                if (map.get(keys[j]) > max) {
                    max = map.get(keys[j]);
                    maxElement = (Integer) keys[j];
                }
            }
            res[i] = maxElement;
            map.put(maxElement, -1);
        }
        return res;
    }
}
