class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = (r + l) // 2
            time = sum([math.ceil(p / m) for p in piles])
            if time <= h:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res