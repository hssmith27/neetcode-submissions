class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')', '{':'}', '[':']'}
        stack = []

        for i in range(len(s)):
            if s[i] in mapping:
                stack = stack + [mapping[s[i]]]
            else:
                if not stack:
                    return False
                nextChar = stack.pop()
                if nextChar != s[i]:
                    return False

        return not stack