class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        chars = defaultdict(int)
        l, r = 0, 0

        while r < len(s):
            chars[s[r]] += 1
            while chars[s[r]] > 1:
                chars[s[l]] -= 1
                l += 1
            r += 1
            res = max(res, r - l)

        return res

