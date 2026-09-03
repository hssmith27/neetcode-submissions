class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left = 0
        right = 0

        while right < len(prices):
            res = max(res, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left += 1
            else:
                right += 1

        return res