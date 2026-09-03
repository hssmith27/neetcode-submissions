class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {'(' : ')', '{' : '}', '[' : ']'}

        for i in range(len(s)):
            char = s[i]
            if char in ['(', '{', '[']:
                stack.append(bracketMap[char])
            elif len(stack) == 0 or stack.pop() != char:
                return False

        return len(stack) == 0