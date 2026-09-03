class Solution {
    public boolean isHappy(int n) {
        int slow = n, fast = conversion(n);

        while (slow != fast) {
            fast = conversion(fast);
            fast = conversion(fast);
            slow = conversion(slow);
        }

        return fast == 1;
    }

    private int conversion(int n) {
        int result = 0;
        while (n != 0) {
            result += (n % 10) * (n % 10);
            n = n / 10;
        }
        return result;
    }
}
