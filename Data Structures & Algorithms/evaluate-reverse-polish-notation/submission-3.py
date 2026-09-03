class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                firstVal = stack.pop()
                secondVal = stack.pop()
                stack.append(firstVal + secondVal)
            elif token == "-":
                firstVal = stack.pop()
                secondVal = stack.pop()
                stack.append(secondVal - firstVal)
            elif token == "*":
                firstVal = stack.pop()
                secondVal = stack.pop()
                stack.append(secondVal * firstVal)
            elif token == "/":
                firstVal = stack.pop()
                secondVal = stack.pop()
                stack.append(int(secondVal / firstVal))
            else:
                stack.append(int(token))
        
        return stack.pop()