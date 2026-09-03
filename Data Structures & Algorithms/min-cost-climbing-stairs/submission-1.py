class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]

        total = [0] * len(cost)
        total[-1] = cost[-1]
        total[-2] = cost[-2]

        index = len(cost) - 3
        while index >= 0:
            print("WOW")
            total[index] = cost[index] + min(total[index + 1], total[index + 2])
            index -= 1

        return min(total[0], total[1])