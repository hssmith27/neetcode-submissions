class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sChars, tChars = [0] * 26, [0] * 26

        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]

            sChars[ord(sChar) - ord('a')] += 1
            tChars[ord(tChar) - ord('a')] += 1

        return sChars == tChars