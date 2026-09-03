class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        l, r = 0, 0
        maxLength = 0

        while r < len(s):
            nextChar = s[r]
            while nextChar in chars:
                chars.pop(s[l])
                l += 1
            chars[nextChar] = 1
            maxLength = max(maxLength, r - l + 1)
            r += 1

        return maxLength
