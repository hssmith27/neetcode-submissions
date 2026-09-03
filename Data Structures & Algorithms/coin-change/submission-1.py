class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        i = 1
        while i < amount + 1:
            minCoins = -1

            for coin in coins:
                prev = i - coin
                if prev >= 0 and dp[prev] != -1:
                    if minCoins == -1 or dp[prev] + 1 < minCoins:
                        minCoins = dp[prev] + 1
                
            dp[i] = minCoins
            i += 1

        print(dp)
        return dp[amount]