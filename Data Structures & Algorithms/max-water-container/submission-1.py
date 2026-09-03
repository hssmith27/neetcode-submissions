class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                water = 0
                minHeight = min(heights[i], heights[j]) 
                water += minHeight * (j - i)

                if water > maxWater:
                    maxWater = water
        return maxWater