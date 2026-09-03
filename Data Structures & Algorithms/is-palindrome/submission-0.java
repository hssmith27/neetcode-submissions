class Solution {
    public boolean isPalindrome(String s) {
        String string = s.replaceAll("[^a-zA-Z0-9]", "");
        string = string.toLowerCase();
        int start = 0;
        int end = string.length() - 1;
        

        for (int i = 0; i < string.length() / 2; i++) {
            if (string.charAt(start) != string.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }

        return true;
    }
}
