class Solution:
    def isValid(self, s: str) -> bool:
        # Stack, for each open bracket, add a closed bracket
        # Make sure they close in proper order, if don't we return False
        brackets = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []

        for char in s:
            if char in brackets:
                stack.append(brackets[char])
            else:
                if not stack or char != stack.pop():
                    return False

        return len(stack) == 0