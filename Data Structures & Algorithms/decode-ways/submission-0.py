class Solution:
    def numDecodings(self, s: str) -> int:
        def backtrack(i):
            if i == len(s):
                return 1
            first = 0
            second = 0
            if s[i] != "0":
                first = backtrack(i + 1)

            if i < len(s) - 1:
                if self.isValid(s[i: i + 2]):
                    second = backtrack(i + 2)
            return first + second
    
        return backtrack(0)

    def isValid(self, string):
        num = int(string)
        return 9 < num < 27
