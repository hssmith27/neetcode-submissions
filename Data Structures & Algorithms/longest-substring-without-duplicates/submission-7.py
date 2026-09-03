class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        l, r = 0, 0
        res = 0

        while r < len(s):
            nextChar = s[r]
            if nextChar in chars:
                l = max(chars[nextChar] + 1, l)
            chars[nextChar] = r
            r += 1
            res = max(res, r - l)

        return res