class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = {}

        for character in s.lower():
            chars[character] = chars.get(character, 0) + 1

        for character in t.lower():
            chars[character] = chars.get(character, 0) - 1
            if chars[character] < 0:
                return False

        return True


        