class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        matches = 0
        chars1 = [0] * 26
        chars2 = [0] * 26

        # Iterate over chars of s1 and simultaneously s2
        for i in range(len(s1)):
            chars1[ord(s1[i]) - ord('a')] = chars1[ord(s1[i]) - ord('a')] + 1
            chars2[ord(s2[i]) - ord('a')] = chars2[ord(s2[i]) - ord('a')] + 1

        # Iterate over arrays, find number of matches
        for i in range(len(chars1)):
            if chars1[i] == chars2[i]:
                matches += 1
        
        l = 0
        # Iterate over remaining chars of s2, updating match every time
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            prevChar = s2[l]
            # Updating # of matches
            if chars2[ord(prevChar) - ord('a')] == chars1[ord(prevChar) - ord('a')]:
                matches -= 1
            elif chars2[ord(prevChar) - ord('a')] - 1 == chars1[ord(prevChar) - ord('a')]:
                matches += 1
            # Updating frequencies
            chars2[ord(prevChar) - ord('a')] = chars2[ord(prevChar) - ord('a')] - 1
            l += 1

            nextChar = s2[r]
            # Updating # of matches
            if chars2[ord(nextChar) - ord('a')] == chars1[ord(nextChar) - ord('a')]:
                matches -= 1
            elif chars2[ord(nextChar) - ord('a')] + 1 == chars1[ord(nextChar) - ord('a')]:
                matches += 1
            # Updating frequencies
            chars2[ord(nextChar) - ord('a')] = chars2[ord(nextChar) - ord('a')] + 1
        
        return matches == 26


