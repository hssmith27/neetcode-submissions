class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] char1 = new int[26];
        int[] char2 = new int[26];
        
        for (int i = 0; i < s1.length(); i++) {
            char1[s1.charAt(i) - 'a'] = char1[s1.charAt(i) - 'a'] + 1;
        }

        int left = 0;
        int right = 0;

        while (right < s2.length()) {
            char2[s2.charAt(right) - 'a'] = char2[s2.charAt(right) - 'a'] + 1;
            if (right - left + 1 > s1.length()) {
                char2[s2.charAt(left) - 'a'] = char2[s2.charAt(left) - 'a'] - 1;
                left++;
            }
            if (Arrays.equals(char1, char2)) {
                return true;
            }
            right++;
        }

        return false;
    }
}
