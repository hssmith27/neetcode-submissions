class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        right = 1
        res = 1
        chars = set(s[0])

        while right < len(s):
            next_char = s[right]
            while next_char in chars:
                chars.remove(s[left])
                left += 1
            chars.add(next_char)
            res = max(res, right - left + 1)
            right += 1

        return res