class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        chars1 = [0] * 26
        chars2 = [0] * 26

        for i in range(len(s1)):
            chars1[ord(s1[i]) - ord('a')] = chars1[ord(s1[i]) - ord('a')] + 1
            chars2[ord(s2[i]) - ord('a')] = chars2[ord(s2[i]) - ord('a')] + 1
        
        matches = 0

        for i in range(len(chars1)):
            if chars1[i] == chars2[i]:
                matches += 1

        left = 0
        right = len(s1)

        while right < len(s2):
            if matches == 26:
                return True

            if chars2[ord(s2[left]) - ord('a')] == chars1[ord(s2[left]) - ord('a')]:
                matches -= 1
            chars2[ord(s2[left]) - ord('a')] = chars2[ord(s2[left]) - ord('a')] - 1
            if chars2[ord(s2[left]) - ord('a')] == chars1[ord(s2[left]) - ord('a')]:
                matches += 1
            left += 1

            if chars2[ord(s2[right]) - ord('a')] == chars1[ord(s2[right]) - ord('a')]:
                matches -= 1
            chars2[ord(s2[right]) - ord('a')] = chars2[ord(s2[right]) - ord('a')] + 1
            if chars2[ord(s2[right]) - ord('a')] == chars1[ord(s2[right]) - ord('a')]:
                matches += 1
            right += 1
        
        return matches == 26
            