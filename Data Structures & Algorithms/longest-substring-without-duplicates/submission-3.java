class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.isEmpty()) {
            return 0;
        }
        int res = 1;

        int left = 0;
        int right = 1;

        HashMap<Character, Integer> map = new HashMap<>();
        map.put(s.charAt(left), 1);

        while (right < s.length()) {
            if (map.containsKey(s.charAt(right))) {
                map.put(s.charAt(right), map.get(s.charAt(right)) + 1);
            }
            else {
                map.put(s.charAt(right), 1);
            }
            while (map.containsKey(s.charAt(right)) && map.get(s.charAt(right)) > 1) {
                map.put(s.charAt(left), map.get(s.charAt(left)) - 1);
                left++;
            }
            res = Math.max(res, (right - left) + 1);
            right++;
        }

        return res;
    }
}
