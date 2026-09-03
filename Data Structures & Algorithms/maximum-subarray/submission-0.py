class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        prevMax = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            maxSum = max(num, prevMax + num, maxSum)
            prevMax = max(num, prevMax + num)

        return maxSum