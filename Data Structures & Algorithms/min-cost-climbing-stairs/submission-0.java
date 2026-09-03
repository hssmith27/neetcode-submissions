class Solution {
    public int minCostClimbingStairs(int[] cost) {
        return Math.min(minCostHelper(cost, 0, 0), minCostHelper(cost, 1, 0));
    }

    public int minCostHelper(int[] cost, int step, int totalCost) {
        if (step >= cost.length) {
            return totalCost;
        }
        return Math.min(minCostHelper(cost, step + 1, totalCost + cost[step]), minCostHelper(cost, step + 2, totalCost + cost[step]));
    }
}
