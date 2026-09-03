class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        for (int i = 0; i < s.length(); i++) {
            int length = 1;
            HashMap<Character, Boolean> map = new HashMap<>();
            map.put(s.charAt(i), true);
            for (int j = i + 1; j < s.length(); j++) {
                if (map.containsKey(s.charAt(j))) {
                    break;
                }
                else {
                    map.put(s.charAt(j), true);
                    length++;
                }
            }

            if (length > maxLength) {
                maxLength = length;
            }
        }
        return maxLength;
    }
}
