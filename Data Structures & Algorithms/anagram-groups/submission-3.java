public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> res = new HashMap<>();
        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sortedStr = new String(chars);
            if (res.containsKey(sortedStr)) {
                ArrayList<String> updatedAnagram = res.get(sortedStr);
                updatedAnagram.add(str);
                res.put(sortedStr, updatedAnagram);
            }
            else {
                ArrayList<String> anagram = new ArrayList<>();
                anagram.add(str);
                res.put(sortedStr, anagram);
            }
        }
        return new ArrayList<>(res.values());
    }
}