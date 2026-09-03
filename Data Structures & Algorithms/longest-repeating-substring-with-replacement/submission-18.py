class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l, r = 0, 0
        maxf = 0
        res = 0

        while r < len(s):
            char = s[r]
            counts[char] += 1
            maxf = max(maxf, counts[char])

            while r - l + 1 > k + maxf:
                counts[s[l]] -= 1
                l += 1
            
            r += 1
            res = max(res, r - l)

        return res
