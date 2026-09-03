class Solution {
    public String encode(List<String> strs) {
        String res = "";
        for (String str : strs) {
            res += str.length();
            res += "#";
            res += str;
        }
        return res;
    }

    public List<String> decode(String str) {
        ArrayList<String> res = new ArrayList();
        int i = 0;

        while (i < str.length()) {
            int start = i;
            while (str.charAt(i) != '#') {
                i++;
            }
            int end = i;
            int length = Integer.parseInt(str.substring(start, end));
            String substr = str.substring(i + 1, i + 1 + length);
            res.add(substr);
            i += length + 1;
        }
        return res;
    }
}
