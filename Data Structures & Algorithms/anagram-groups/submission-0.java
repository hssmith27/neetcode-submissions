class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> groups = new ArrayList<>();
        List<String> words = new ArrayList<>();
        Collections.addAll(words, strs);

        while (words.size() > 0) {
            List<String> group = new ArrayList<>();
            group.add(words.remove(0));
            for (int i = 0; i < words.size(); i++) {
                if (isAnagram(group.get(0), words.get(i))) {
                    group.add(words.remove(i));
                    i--;
                }
            }
            groups.add(group);
        }
        return groups;
    }

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            }
            else {
                map.put(c, 1);
            }
        }

        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            if (map.containsKey(c)) {
                if (map.get(c) > 0) {
                    map.put(c, map.get(c) - 1);
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
