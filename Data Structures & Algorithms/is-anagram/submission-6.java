class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> chars = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            if (chars.containsKey(current)) {
                chars.put(current, chars.get(current) + 1);
            }
            else {
                chars.put(current, 1);
            }
        }

        for (int i = 0; i < t.length(); i++) {
            char current = t.charAt(i);
            if (chars.containsKey(current)) {
                if (chars.get(current) == 0) {
                    return false;
                }
                chars.put(current, chars.get(current) - 1);
            }
            else {
                return false;
            }
        }

        return true;
    }
}
