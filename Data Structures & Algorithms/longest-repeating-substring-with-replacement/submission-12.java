class Solution {
    public int characterReplacement(String s, int k) {
        int res = 0;
        HashMap<Character, Integer> map = new HashMap<>();

        int left = 0;
        int right = 0;
        int maxFreq = 0;

        while (right < s.length()) {
            map.put(s.charAt(right), map.getOrDefault(s.charAt(right), 0) + 1);
            maxFreq = Math.max(maxFreq, map.get(s.charAt(right)));

            while (right - left + 1 - maxFreq > k) {
                map.put(s.charAt(left), map.get(s.charAt(left)) - 1);
                left++;
            }

            res = Math.max(res, right - left + 1);
            right++;
        }

        return res;
    }
}
