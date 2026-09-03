class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        ways = [1, 2] + ([0] * (n - 2))
        i = 2
        while i < len(ways):
            ways[i] = ways[i - 1] + ways[i - 2]
            i += 1

        return ways[n - 1]
