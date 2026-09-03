class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l, r = 0, 0
        res = 0

        while r < len(s):
            char = s[r]
            while char in chars:
                chars.remove(s[l])
                l += 1
            chars.add(char)
            r += 1
            res = max(res, r - l)

        return res