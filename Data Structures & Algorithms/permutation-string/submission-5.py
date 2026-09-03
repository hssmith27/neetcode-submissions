class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        chars1 = [0] * 26
        chars2 = [0] * 26

        for i in range(len(s1)):
            chars1[ord(s1[i]) - ord('a')] += 1
            chars2[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(len(chars1)):
            if chars1[i] == chars2[i]:
                matches += 1

        l, r = 0, len(s1)
        while r < len(s2):
            if matches == 26:
                return True

            if chars2[ord(s2[l]) - ord('a')] == chars1[ord(s2[l]) - ord('a')]:
                matches -= 1
            elif chars2[ord(s2[l]) - ord('a')] - 1 == chars1[ord(s2[l]) - ord('a')]:
                matches += 1
            chars2[ord(s2[l]) - ord('a')] -= 1
            l += 1

            if chars2[ord(s2[r]) - ord('a')] == chars1[ord(s2[r]) - ord('a')]:
                matches -= 1
            elif chars2[ord(s2[r]) - ord('a')] + 1 == chars1[ord(s2[r]) - ord('a')]:
                matches += 1
            chars2[ord(s2[r]) - ord('a')] += 1
            r += 1
            
        return matches == 26