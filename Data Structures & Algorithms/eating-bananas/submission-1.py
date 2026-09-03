class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        res = max(piles)

        max_val = max(piles)

        def eat_bananas(rate, piles):
            time = 0
            for i in range(len(piles)):
                time += math.ceil(float(piles[i]) / rate)

            return time

        while k <= max_val:
            m = (max_val + k) // 2
            time = eat_bananas(m, piles)
            if time <= h:
                res = m
                max_val = m - 1
            else:
                k = m + 1
        
        return res