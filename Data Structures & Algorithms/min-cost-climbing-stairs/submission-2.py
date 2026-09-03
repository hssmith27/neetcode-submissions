class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]

        i = len(dp) - 3
        while i >= 0:
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
            i -= 1

        return min(dp[0], dp[1])
