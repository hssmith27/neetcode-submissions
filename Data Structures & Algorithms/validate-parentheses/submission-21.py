class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {'(' : ')', '{' : '}', '[' : ']'}

        for i in range(len(s)):
            char = s[i]
            if char in ['(', '{', '[']:
                stack.append(bracketMap[char])
            elif not stack or stack.pop() != char:
                return False

        return not stack