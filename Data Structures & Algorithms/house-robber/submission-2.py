class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        values = [0] * len(nums)
        values[-1] = nums[-1]
        values[-2] = nums[-2]
        values[-3] = nums[-3] + nums[-1]
        
        index = len(nums) - 4
        while index >= 0:
            values[index] = nums[index] + max(values[index + 2], values[index + 3])
            index -= 1
        print(values)

        return max(values[0], values[1])