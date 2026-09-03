class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        res = 0

        maxf = 0
        l, r = 0, 0

        while r < len(s):
            counts[s[r]] += 1
            maxf = max(maxf, counts[s[r]])

            while r - l + 1 > maxf + k:
                counts[s[l]] -= 1
                l += 1

            r += 1
            res = max(res, r - l)

        return res