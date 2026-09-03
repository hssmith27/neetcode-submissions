class Solution {
    public int[] plusOne(int[] digits) {
        int[] result = digits;
        if (digits[digits.length - 1] != 9) {
            result[digits.length - 1] = digits[digits.length - 1] + 1;
        }
        else {
            int digit = digits.length - 1;
            while (digit >= 0 && digits[digit] == 9) {
                result[digit] = 0;
                digit--;
            }
            if (digit < 0) {
                int[] newResult = new int[result.length + 1];
                newResult[0] = 1;
                for (int i = 0; i < result.length; i++) {
                    newResult[i + 1] = result[i];
                }
                return newResult;
            }
            else if (result[digit + 1] == 0) {
                result[digit] = digits[digit] + 1;
            }
        }
        return result;
    }
}
