class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sChars = [0] * 26
        tChars = [0] * 26

        # Count number of each char in s and t
        for i in range(len(s)):
            sChars[ord(s[i]) - ord('a')] += 1
            tChars[ord(t[i]) - ord('a')] += 1

        return sChars == tChars

