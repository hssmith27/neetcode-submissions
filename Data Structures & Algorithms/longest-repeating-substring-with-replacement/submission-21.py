class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        res = 0
        maxf = 0
        chars = defaultdict(int)

        while r < len(s):
            chars[s[r]] += 1
            maxf = max(maxf, chars[s[r]])
            while maxf + k < r - l + 1:
                chars[s[l]] -= 1
                l += 1

            r += 1
            res = max(res, r - l)

        return res
