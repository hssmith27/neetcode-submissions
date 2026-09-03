class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {'(' : ')', '{' : '}', '[' : ']'}

        for i in range(len(s)):
            char = s[i]
            if char in bracket_map:
                stack.append(bracket_map[char])
            elif len(stack) == 0:
                return False
            elif stack.pop() != char:
                    return False

        return len(stack) == 0