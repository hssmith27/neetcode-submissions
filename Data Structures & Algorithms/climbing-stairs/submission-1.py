class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        methods = [0] * n
        methods[-1] = 1
        methods[-2] = 2
        for i in range(n - 3, -1, -1):
            methods[i] = methods[i + 1] + methods[i + 2]

        return methods[0]