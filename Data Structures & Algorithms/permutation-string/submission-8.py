class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = 0
        r = 0

        s1Chars, s2Chars = [0] * 26, [0] * 26

        while r < len(s1):
            s1Chars[ord(s1[r]) - ord('a')] += 1
            s2Chars[ord(s2[r]) - ord('a')] += 1
            r += 1
        
        while r < len(s2):
            if s1Chars == s2Chars:
                return True
            s2Chars[ord(s2[l]) - ord('a')] -= 1
            l += 1
            s2Chars[ord(s2[r]) - ord('a')] += 1
            r += 1

        return s1Chars == s2Chars
        