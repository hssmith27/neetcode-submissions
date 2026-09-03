class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        int index = 0;
        while (index < tokens.length) {
            if (tokens[index].equals("+")) {
                int first = stack.pop();
                int second = stack.pop();
                stack.push(first + second);
            }
            else if (tokens[index].equals("-")) {
                int first = stack.pop();
                int second = stack.pop();
                stack.push(second - first);
            }
            else if (tokens[index].equals("*")) {
                int first = stack.pop();
                int second = stack.pop();
                stack.push(first * second);
            }
            else if (tokens[index].equals("/")) {
                int first = stack.pop();
                int second = stack.pop();
                stack.push((int)(second / first));
            }
            else {
                stack.push(Integer.parseInt(tokens[index]));
            }

            index++;
        }

        return stack.pop();
    }
}
