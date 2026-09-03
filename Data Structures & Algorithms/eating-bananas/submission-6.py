class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mink, maxk = 1, max(piles)
        bestk = maxk

        while mink <= maxk:
            k = (maxk - mink) // 2 + mink
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / k)
            if totalHours <= h:
                bestk = k
                maxk = k - 1
            else:
                mink = k + 1

        return bestk