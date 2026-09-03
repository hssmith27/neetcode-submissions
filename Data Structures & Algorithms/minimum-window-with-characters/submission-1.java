class Solution {
    public String minWindow(String s, String t) {
        String res = "";

        HashMap<Character, Integer> smap = new HashMap<>();
        HashMap<Character, Integer> tmap = new HashMap<>();

        int matches = 0;
        int neededMatches = 0;

        for (int i = 0; i < t.length(); i++) {
            tmap.put(t.charAt(i), tmap.getOrDefault(t.charAt(i), 0) + 1);
            if (tmap.get(t.charAt(i)) == 1) {
                neededMatches++;
            }
        }

        int left = 0;
        int right = 0;

        while (right < s.length()) {
            char cur = s.charAt(right);
            smap.put(cur, smap.getOrDefault(cur, 0) + 1);

            if (smap.get(cur) == tmap.get(cur)) {
                matches++;
            }

            while (matches == neededMatches) {
                // Update res
                String sub = s.substring(left, right + 1);
                if (sub.length() < res.length() || res.isEmpty()) {
                    res = sub;
                }

                char leftChar = s.charAt(left);

                // Contract Window
                smap.put(leftChar, smap.get(leftChar) - 1);
                if (tmap.containsKey(leftChar) && smap.get(leftChar) < tmap.get(leftChar)) {
                    matches--;
                }
                left++;
            }

            right++;
        }

        return res;
    }
}
