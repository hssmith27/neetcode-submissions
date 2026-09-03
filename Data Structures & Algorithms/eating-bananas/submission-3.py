class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = max(piles)

        while l <= r:
            rate = (r + l) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / rate)
            if time <= h:
                k = min(k, rate)
                r = rate - 1
            else:
                l = rate + 1
            

        return k