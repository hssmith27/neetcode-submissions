class Solution:
    def trap(self, height: List[int]) -> int:
        right = [0]
        rightMax = 0
        left = [0]
        leftMax = 0
        for i in range(1, len(height)):
            if height[i - 1] > leftMax:
                leftMax = height[i - 1]
            left.append(leftMax)

        for i in reversed(range(0, len(height) - 1)):
            if height[i + 1] > rightMax:
                rightMax = height[i + 1]
            right.insert(0, rightMax)
        totalWater = 0

        print(left)
        print(right)
        for i in range(1, len(height) - 1):
            if height[i] <= min(left[i], right[i]):
                totalWater += min(left[i], right[i]) - height[i]

        return totalWater