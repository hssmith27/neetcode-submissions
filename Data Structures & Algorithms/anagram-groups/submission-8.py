class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars_to_strs = {}

        for word in strs:
            chars = [0] * 26
            for char in word:
                chars[ord(char) - ord('a')] += 1
            chars_to_strs[tuple(chars)] = chars_to_strs.get(tuple(chars), []) + [word]
        return list(chars_to_strs.values())