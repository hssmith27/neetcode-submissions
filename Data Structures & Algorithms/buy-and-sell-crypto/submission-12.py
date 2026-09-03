class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        res = 0

        while r < len(prices):
            res = max(res, prices[r] - prices[l])
            if prices[r] >= prices[l]:
                r += 1
            else: 
                l += 1

        return res