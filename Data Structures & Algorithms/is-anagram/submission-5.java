class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> chars = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (chars.containsKey(s.charAt(i))) {
                chars.put(s.charAt(i), chars.get(s.charAt(i)) + 1);
            }
            else {
                chars.put(s.charAt(i), 1);
            }
        }

        for (int i = 0; i < t.length(); i++) {
            if (chars.containsKey(t.charAt(i))) {
                if (chars.get(t.charAt(i)) >= 1) {
                    chars.put(t.charAt(i), chars.get(t.charAt(i)) - 1);
                }
                else {
                    return false;
                }
            }
            else {
                return false;
            }
        }
        return true;
    }
}
