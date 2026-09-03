class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> map = new HashMap<>();

        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c== '[') {
                stack.push(c);
            }
            else if (map.containsKey(c)) {
                if (stack.isEmpty()) {
                    return false;
                }
                char next = stack.pop();
                if (map.get(c) != next) {
                    return false;
                }
            }
            else {
                return false;
            }
        }

        return stack.isEmpty();
    }
}
